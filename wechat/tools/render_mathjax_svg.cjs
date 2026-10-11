#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { createRequire } = require("module");

function candidatePackageRoots() {
  const roots = [];
  const configured = process.env.WOEAI_MATHJAX_NODE_MODULE_DIR;
  if (configured) {
    const resolved = path.resolve(configured);
    roots.push(resolved.endsWith("node_modules") ? path.dirname(resolved) : resolved);
  }
  roots.push(process.cwd());
  roots.push(path.resolve(__dirname, "../.."));
  const scratchRoot = "/tmp/woeai-formula-render-node";
  if (fs.existsSync(path.join(scratchRoot, "package.json"))) {
    roots.push(scratchRoot);
  }
  return [...new Set(roots)];
}

function loadMathJax() {
  for (const root of candidatePackageRoots()) {
    const packageJson = path.join(root, "package.json");
    try {
      const req = fs.existsSync(packageJson) ? createRequire(packageJson) : require;
      return {
        mathjax: req("mathjax-full/js/mathjax.js").mathjax,
        TeX: req("mathjax-full/js/input/tex.js").TeX,
        SVG: req("mathjax-full/js/output/svg.js").SVG,
        liteAdaptor: req("mathjax-full/js/adaptors/liteAdaptor.js").liteAdaptor,
        RegisterHTMLHandler: req("mathjax-full/js/handlers/html.js").RegisterHTMLHandler,
        AllPackages: req("mathjax-full/js/input/tex/AllPackages.js").AllPackages,
      };
    } catch (error) {
      continue;
    }
  }
  throw new Error(
    "Missing mathjax-full. Install it for local rendering, for example: " +
      "npm --prefix /tmp/woeai-formula-render-node install mathjax-full"
  );
}

function readStdin() {
  return fs.readFileSync(0, "utf8");
}

function escapeAttribute(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function appendStyle(existingStyle, extraStyle) {
  const trimmed = String(existingStyle ?? "").trim();
  if (!trimmed) {
    return extraStyle;
  }
  return `${trimmed.replace(/;*$/, ";")}${extraStyle}`;
}

function addOrAppendStyle(attrs, extraStyle) {
  if (/\sstyle="/.test(attrs)) {
    return attrs.replace(/\sstyle="([^"]*)"/, (_match, style) => {
      return ` style="${appendStyle(style, extraStyle)}"`;
    });
  }
  return `${attrs} style="${extraStyle}"`;
}

function centerDisplaySvg(rendered, formula) {
  if (!formula.display) {
    return rendered;
  }
  return rendered.replace(/<svg\b([^>]*)>/, (_match, attrs) => {
    const styledAttrs = addOrAppendStyle(
      attrs,
      "display:inline-block;margin:0 auto;max-width:100%;"
    );
    return `<svg${styledAttrs}>`;
  });
}

// WeChat's SVG guidance recommends currentColor. Pair presentation
// attributes with inline paint styles, and use standard HTML containers.
// Reference: doocs/md packages/core/src/extensions/katex.ts (2026-10-11).
// This must still be checked in the actual phone reader after API delivery.
function withInheritedPaint(rendered) {
  const viewBox = rendered.match(/<svg\b[^>]*\bviewBox="([^"]+)"/);
  const values = viewBox ? viewBox[1].trim().split(/\s+/).map(Number) : [];
  if (values.length !== 4 || !values.every(Number.isFinite) || values[2] <= 0 || values[3] <= 0) {
    throw new Error("Formula SVG requires a finite positive viewBox");
  }
  return rendered.replace(/<g\b([^>]*)>/, (_match, attrs) => {
    const painted = addOrAppendStyle(attrs, "fill:currentColor;stroke:currentColor;");
    return `<g${painted}>`;
  });
}

function withFormulaMetadata(rendered, formula) {
  if (/data-mjx-error=|data-mml-node="merror"/.test(rendered)) {
    throw new Error("MathJax could not render this formula");
  }
  const tex = String(formula.tex ?? "");
  const formulaType = formula.display ? "block-equation" : "inline-equation";
  const metadata = ` data-formula="${escapeAttribute(tex)}" data-formula-type="${formulaType}"`;
  const containerStyle = formula.display
    ? "display:block;text-align:center;margin:0 auto;max-width:100%;overflow-x:auto;"
    : "display:inline-block;vertical-align:middle;";
  const containerTag = formula.display ? "section" : "span";
  const withContainer = rendered.replace(/<mjx-container\b([^>]*)>/, (_match, attrs) => {
    const styledAttrs = addOrAppendStyle(attrs, containerStyle);
    return `<${containerTag}${metadata}${styledAttrs}>`;
  });
  const standardContainer = withContainer.replace(/<\/mjx-container>/g, `</${containerTag}>`);
  return withInheritedPaint(centerDisplaySvg(standardContainer, formula));
}

function main() {
  const input = JSON.parse(readStdin());
  const formulas = Array.isArray(input.formulas) ? input.formulas : [];
  const mj = loadMathJax();
  const adaptor = mj.liteAdaptor();
  mj.RegisterHTMLHandler(adaptor);
  // Do not silently turn unsupported TeX into red literal text.
  const packages = mj.AllPackages.filter((name) => !["noerrors", "noundefined"].includes(name));
  const tex = new mj.TeX({ packages });
  const svg = new mj.SVG({ fontCache: "none" });
  const html = mj.mathjax.document("", { InputJax: tex, OutputJax: svg });
  const items = formulas.map((formula, index) => {
    const id = String(formula.id ?? index);
    const node = html.convert(String(formula.tex ?? ""), { display: Boolean(formula.display) });
    return { id, html: withFormulaMetadata(adaptor.outerHTML(node), formula) };
  });
  process.stdout.write(JSON.stringify({ ok: true, items }));
}

if (require.main === module) {
  try {
    main();
  } catch (error) {
    process.stdout.write(JSON.stringify({ ok: false, error: error.message }));
    process.exit(1);
  }
}
module.exports = { withFormulaMetadata };
