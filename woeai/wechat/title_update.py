"""An existing draft title change, preserving its current remote article fields."""
from copy import deepcopy


class TitleUpdateError(RuntimeError):
    def __init__(self, code, *, write_attempted=False):
        self.code = code
        self.write_attempted = write_attempted
        super().__init__(code)


def update_title(read_article, write_article, *, expected_title, desired_title):
    """Read twice, write once, then verify; never render or upload any content."""
    before = read_article()
    if any(not isinstance(before.get(key), str) or not before[key] for key in ('title', 'content', 'thumb_media_id')):
        raise TitleUpdateError('incomplete_remote_article')
    if before.get('title') not in {expected_title, desired_title}:
        raise TitleUpdateError('remote_title_conflict')
    current = read_article()
    if current != before:
        raise TitleUpdateError('remote_article_changed')
    if current['title'] == desired_title:
        return {'updated': False, 'title_verified': True, 'non_title_unchanged': True}
    payload = {key: deepcopy(value) for key, value in current.items()
               if key not in {'url', 'thumb_url'}}
    payload['title'] = desired_title
    write_article(payload)
    after = read_article()
    if after.get('title') != desired_title:
        raise TitleUpdateError('title_readback_failed', write_attempted=True)
    before_fields = {key: value for key, value in before.items() if key not in {'title', 'url'}}
    after_fields = {key: value for key, value in after.items() if key not in {'title', 'url'}}
    if after_fields != before_fields:
        raise TitleUpdateError('non_title_readback_changed', write_attempted=True)
    return {'updated': True, 'title_verified': True, 'non_title_unchanged': True}
