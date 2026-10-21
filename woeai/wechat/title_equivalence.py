"""Only the two formatting changes explicitly approved by the account owner."""
from html.parser import HTMLParser
import hashlib
import io
import re
from urllib.error import HTTPError
from urllib.parse import parse_qsl, urlsplit
from urllib.request import HTTPRedirectHandler, build_opener

_CLOSING = re.compile(r"[ \t\r\n]*/?[ \t\r\n]*>$")
_MAX_BYTES = 12 * 1024 * 1024


class _ImageClosings(HTMLParser):
    def __init__(self, content):
        super().__init__(convert_charrefs=False)
        self.content = content
        self.offsets = [0] + [m.end() for m in re.finditer("\n", content)]
        self.tags = []
        self.svg_depth = 0
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        if tag == "svg":
            self.svg_depth += 1
        self._image(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self._image(tag, attrs)

    def handle_endtag(self, tag):
        if tag == "svg":
            self.svg_depth = max(0, self.svg_depth - 1)

    def _image(self, tag, attrs):
        if tag == "img" and not self.svg_depth:
            line, column = self.getpos()
            start = self.offsets[line - 1] + column
            raw = self.get_starttag_text()
            self.tags.append((start, start + len(raw), raw, attrs))

    def canonical(self):
        chunks = []; previous = 0
        for start, end, raw, _attrs in self.tags:
            chunks.extend((self.content[previous:start], _CLOSING.sub(">", raw)))
            previous = end
        chunks.append(self.content[previous:])
        return "".join(chunks)


def image_closing_equivalence(before, after):
    """Preserve every raw character except whitespace/slash at HTML img endings."""
    if not isinstance(before, str) or not isinstance(after, str):
        return {"equivalent": False, "reason": "body_not_string"}
    left, right = _ImageClosings(before), _ImageClosings(after)
    equal = (left.canonical() == right.canonical()
             and [tag[3] for tag in left.tags] == [tag[3] for tag in right.tags])
    return {"equivalent": equal, "reason": "img_closing_only" if equal else "other_body_bytes_changed",
            "changed_image_tags": sum(a[2] != b[2] for a, b in zip(left.tags, right.tags)),
            "before_sha256": hashlib.sha256(before.encode()).hexdigest(),
            "after_sha256": hashlib.sha256(after.encode()).hexdigest()}


def _cdn_url_allowed(url):
    if not isinstance(url, str):
        return False
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError:
        return False
    return (parsed.scheme in {"http", "https"}
            and parsed.hostname in {"mmbiz.qpic.cn", "mmbiz.qlogo.cn"}
            and parsed.username is None and parsed.password is None
            and port is None
            and {k.lower() for k, _ in parse_qsl(parsed.query)} <= {"wx_fmt"}
            and not parsed.fragment)


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        raise HTTPError(request.full_url, code, "cover_redirect_not_followed", headers, fp)


def read_cover_image(url):
    if not _cdn_url_allowed(url):
        raise ValueError("unapproved_cover_url")
    with build_opener(_NoRedirect()).open(url, timeout=30) as response:
        data = response.read(_MAX_BYTES + 1)
    if len(data) > _MAX_BYTES:
        raise ValueError("cover_too_large")
    return data


def cover_url_equivalence(before_url, after_url, fetch_image):
    """Read exactly the supplied CDN URLs once; require bytes AND full pixels."""
    result = {"equivalent": False, "bytes_equal": False, "pixels_equal": None}
    if not _cdn_url_allowed(before_url) or not _cdn_url_allowed(after_url):
        return {**result, "reason": "unapproved_cover_url"}
    try:
        from PIL import Image
        before = fetch_image(before_url)
        after = fetch_image(after_url)
        if not isinstance(before, bytes) or not isinstance(after, bytes) or max(len(before), len(after)) > _MAX_BYTES:
            return {**result, "reason": "invalid_cover_bytes"}
        result.update(before_sha256=hashlib.sha256(before).hexdigest(),
                      after_sha256=hashlib.sha256(after).hexdigest(), bytes_equal=before == after)
        if before != after:
            return {**result, "reason": "cover_bytes_changed"}
        pixels = []
        for data in (before, after):
            image = Image.open(io.BytesIO(data))
            if image.width * image.height > 16_000_000:
                return {**result, "reason": "cover_dimensions_too_large"}
            image.load(); rgba = image.convert("RGBA")
            pixels.append((rgba.size, rgba.tobytes()))
        result.update(pixels_equal=pixels[0] == pixels[1], dimensions=list(pixels[0][0]),
                      before_rgba_sha256=hashlib.sha256(pixels[0][1]).hexdigest(),
                      after_rgba_sha256=hashlib.sha256(pixels[1][1]).hexdigest())
        return {**result, "equivalent": result["pixels_equal"], "reason": "identical_bytes_and_pixels"}
    except HTTPError as error:
        return {**result, "reason": "cover_http_error", "http_status": error.code}
    except Exception as error:
        return {**result, "reason": "cover_verification_unavailable", "error_type": type(error).__name__}
