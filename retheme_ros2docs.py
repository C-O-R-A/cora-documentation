#!/usr/bin/env python3
"""
retheme_ros2docs.py
────────────────────────────────────────────────────────────────────────────
Post-processes rosdoc2 HTML output to replace sphinx_rtd_theme with the
CORA dark theme. Run automatically by `make ros2docs` after rosdoc2 finishes.

What it does per HTML file:
  1. Strips all sphinx_rtd_theme CSS/JS <link> and <script> tags
  2. Injects the CORA CSS (relative path back to the shared static dir)
  3. Rewrites the <body> class to remove RTD classes
  4. Wraps the RTD content div structure in CORA layout divs
  5. Injects the CORA topbar and sidebar chrome

Usage:
    python3 retheme_ros2docs.py <html_root>

    where <html_root> is _build/html/api/ros2/
"""

import sys
import re
from pathlib import Path

# ── RTD patterns to strip ─────────────────────────────────────────────────
RTD_CSS_PATTERNS = [
    r'<link[^>]+sphinx_rtd_theme[^>]*>',
    r'<link[^>]+_static/css/theme\.css[^>]*>',
    r'<link[^>]+_static/css/badge_only\.css[^>]*>',
    r'<link[^>]+_static/pygments\.css[^>]*>',
    r'<link[^>]+_static/css/fonts[^>]*>',
]
RTD_JS_PATTERNS = [
    r'<script[^>]+sphinx_rtd_theme[^>]*>.*?</script>',
    r'<script[^>]+_static/js/theme\.js[^>]*>.*?</script>',
    r'<script[^>]+_static/js/versions\.js[^>]*>.*?</script>',
]

# ── CORA topbar HTML (injected at top of <body>) ───────────────────────────
# Sidebar nav is rebuilt from the RTD .wy-nav-side content
CORA_TOPBAR = """
<header class="cora-topbar">
  <div class="cora-topbar-logo">
    <a href="{root}index.html">
      <div class="cora-logo-mark">CORA</div>
      <div class="cora-logo-sub">Docs</div>
    </a>
  </div>
  <div class="cora-topbar-search">
    <form class="cora-search-form" action="{root}../../search.html" method="get">
      <input class="cora-search-input" type="text" name="q"
             placeholder="Search documentation\u2026" />
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
  </div>
  <div class="cora-topbar-meta">
    <span class="cora-version-badge">v{version}</span>
    <a class="cora-topbar-link"
       href="https://github.com/your-org/cora">GitHub</a>
    <a class="cora-topbar-link"
       href="{root}../../pages/changelog.html">Changelog</a>
  </div>
</header>
"""

# ── CSS injected into <head> ──────────────────────────────────────────────
CORA_HEAD_INJECT = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap">
  <link rel="stylesheet" href="{css_path}">
"""

# ── JS injected before </body> ────────────────────────────────────────────
CORA_FOOT_JS = """
<script>
(function() {
  // Highlight active TOC link on scroll
  var links = document.querySelectorAll('.cora-toc-panel a');
  if (!links.length) return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        links.forEach(function(l) { l.classList.remove('active'); });
        var id = e.target.getAttribute('id');
        var m = document.querySelector('.cora-toc-panel a[href="#' + id + '"]');
        if (m) m.classList.add('active');
      }
    });
  }, { rootMargin: '-10% 0px -80% 0px' });
  document.querySelectorAll('h2[id], h3[id]').forEach(function(h) {
    observer.observe(h);
  });
})();
</script>
"""


def depth_to_root(html_file: Path, ros2_root: Path) -> str:
    """Return a relative path prefix from this file back to _build/html/."""
    rel = html_file.relative_to(ros2_root.parent.parent)  # relative to _build/html/
    depth = len(rel.parts) - 1  # number of dirs above the file
    return "../" * depth if depth > 0 else "./"


def strip_rtd_assets(html: str) -> str:
    """Remove all RTD CSS and JS references."""
    for pat in RTD_CSS_PATTERNS + RTD_JS_PATTERNS:
        html = re.sub(pat, "", html, flags=re.DOTALL | re.IGNORECASE)
    return html


def inject_cora_head(html: str, css_rel: str) -> str:
    """Inject CORA fonts and CSS into <head>."""
    inject = CORA_HEAD_INJECT.format(css_path=css_rel)
    return html.replace("</head>", inject + "</head>", 1)


def rewrite_body(html: str, root_rel: str, version: str) -> str:
    """
    Replace the RTD layout structure with the CORA layout.

    RTD structure:
        <body class="wy-body-for-nav">
          <div class="wy-grid-for-nav">
            <nav class="wy-nav-side">...</nav>
            <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">
              <div class="wy-nav-content">
                <div class="rst-content">
                  ... actual content ...
                </div>
              </div>
            </section>
          </div>
        </body>

    CORA structure:
        <body>
          <header class="cora-topbar">...</header>
          <div class="cora-layout">
            <nav class="cora-sidebar">...</nav>    ← rebuilt from wy-nav-side
            <main class="cora-main">
              <div class="cora-content">
                ... actual content ...
              </div>
            </main>
            <aside class="cora-toc-panel">...</aside>  ← rebuilt from local toc
          </div>
        </body>
    """
    # 1. Clean body classes
    html = re.sub(
        r'<body[^>]*class="[^"]*wy-body-for-nav[^"]*"[^>]*>',
        "<body>",
        html,
        flags=re.IGNORECASE,
    )

    # 2. Extract sidebar nav content from RTD
    sidebar_match = re.search(
        r'<nav[^>]+class="[^"]*wy-nav-side[^"]*"[^>]*>(.*?)</nav>',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    sidebar_inner = sidebar_match.group(1) if sidebar_match else ""

    # 3. Extract local TOC if present
    toc_match = re.search(
        r'<div[^>]+class="[^"]*toctree-wrapper[^"]*"[^>]*>.*?</div>',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    # Also look for the inline contents block RTD generates
    contents_match = re.search(
        r'<div[^>]+class="[^"]*contents[^"]*"[^>]*>(.*?)</div>',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    toc_inner = ""
    if contents_match:
        toc_inner = contents_match.group(0)

    # 4. Extract actual page content from rst-content
    content_match = re.search(
        r'<div[^>]+class="[^"]*rst-content[^"]*"[^>]*>(.*?)'
        r'(?=<footer|<div[^>]+class="[^"]*footer)',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    content_inner = content_match.group(1).strip() if content_match else ""

    # 5. Build CORA sidebar from RTD nav
    # Convert RTD nav links to CORA nav-item classes
    cora_sidebar = _convert_rtd_sidebar(sidebar_inner)

    # 6. Assemble topbar
    topbar = CORA_TOPBAR.format(root=root_rel, version=version)

    # 7. Build new body
    new_body = f"""
<body>
{topbar}
<div class="cora-layout">

  <nav class="cora-sidebar" id="cora-sidebar">
{cora_sidebar}
  </nav>

  <main class="cora-main">
    <div class="cora-content">
{content_inner}
    </div>
  </main>

  <aside class="cora-toc-panel" id="cora-toc-panel">
    <div class="cora-toc-panel-label">On this page</div>
{toc_inner}
  </aside>

</div>
"""

    # Replace everything between <body> and </body>
    html = re.sub(
        r"<body>.*</body>",
        new_body + "\n</body>",
        html,
        flags=re.DOTALL,
    )
    return html


def _convert_rtd_sidebar(rtd_nav: str) -> str:
    """
    Convert RTD sidebar HTML to CORA nav-section structure.
    RTD uses <ul> with <li class="toctree-l1"> etc.
    We wrap each top-level group in a cora-nav-section.
    """
    if not rtd_nav.strip():
        return ""

    # Find all top-level caption groups (RTD uses <p class="caption">)
    # and the <ul> that follows each one
    sections = []
    parts = re.split(
        r'(<p[^>]+class="[^"]*caption[^"]*"[^>]*>.*?</p>)',
        rtd_nav,
        flags=re.DOTALL | re.IGNORECASE,
    )

    current_label = "Contents"
    for part in parts:
        caption_match = re.search(
            r'<span[^>]+class="caption-text"[^>]*>(.*?)</span>',
            part, re.DOTALL | re.IGNORECASE
        )
        if caption_match:
            current_label = re.sub(r"<[^>]+>", "", caption_match.group(1)).strip()
        elif "<ul" in part:
            # Convert RTD <li> entries to cora-nav-item links
            items = re.findall(
                r'<li[^>]*class="[^"]*toctree-l1[^"]*"[^>]*>.*?'
                r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>',
                part,
                re.DOTALL | re.IGNORECASE,
            )
            if items:
                nav_items = "\n".join(
                    f'        <a class="cora-nav-item" href="{href}">'
                    f'<span class="cora-nav-icon"></span> '
                    f'{re.sub(r"<[^>]+>", "", text).strip()}</a>'
                    for href, text in items
                )
                sections.append(
                    f'    <div class="cora-nav-section open">\n'
                    f'      <div class="cora-nav-section-header" '
                    f'onclick="coraToggleSection(this)">\n'
                    f'        <span class="cora-nav-section-label">'
                    f'{current_label}</span>\n'
                    f'        <span class="cora-chevron">\u25b6</span>\n'
                    f'      </div>\n'
                    f'      <div class="cora-nav-items">\n'
                    f'{nav_items}\n'
                    f'      </div>\n'
                    f'    </div>\n'
                    f'    <hr class="cora-nav-divider">'
                )
    return "\n".join(sections)


def inject_footer_js(html: str) -> str:
    return html.replace("</body>", CORA_FOOT_JS + "\n</body>", 1)


def process_file(html_file: Path, ros2_root: Path, version: str) -> None:
    try:
        raw = html_file.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  skip {html_file.name}: {e}")
        return

    # Skip non-page files
    if "<html" not in raw.lower():
        return

    # Skip pure redirect files — these are stub pages written by the Makefile
    if 'http-equiv="refresh"' in raw and len(raw) < 600:
        return

    # Skip Sphinx-generated stub pages at the top level of api/ros2/
    # Only process genuine rosdoc2 output which lives in <pkg>/<pkg>/ subdirs
    rel = html_file.relative_to(ros2_root)
    if len(rel.parts) < 3:
        return

    root_rel  = depth_to_root(html_file, ros2_root)
    # Path from this file back to the shared _static dir in _build/html/
    css_rel   = root_rel + "_static/cora.css"

    out = raw
    out = strip_rtd_assets(out)
    out = inject_cora_head(out, css_rel)
    out = rewrite_body(out, root_rel, version)
    out = inject_footer_js(out)

    html_file.write_text(out, encoding="utf-8")


def copy_cora_css(ros2_root: Path) -> None:
    """Copy cora.css into the shared _build/html/_static/ dir if not there."""
    static_dir = ros2_root.parent.parent / "_static"
    static_dir.mkdir(parents=True, exist_ok=True)
    dst = static_dir / "cora.css"
    if dst.exists():
        return
    # Try to find it relative to this script (cora_docs/_theme/cora/static/)
    script_dir = Path(__file__).parent
    src = script_dir / "_theme" / "cora" / "static" / "cora.css"
    if src.exists():
        import shutil
        shutil.copy2(src, dst)
        print(f"  copied cora.css → {dst}")
    else:
        print(f"  ⚠  cora.css not found at {src} — copy it manually to {dst}")


def main() -> None:
    if len(sys.argv) < 2:
        ros2_root = Path("_build/html/api/ros2")
    else:
        ros2_root = Path(sys.argv[1])

    if not ros2_root.exists():
        print(f"error: {ros2_root} does not exist")
        sys.exit(1)

    # Try to read version from conf.py
    version = "0.1"
    conf = Path(__file__).parent / "conf.py"
    if conf.exists():
        m = re.search(r'^version\s*=\s*["\']([^"\']+)["\']', conf.read_text(), re.M)
        if m:
            version = m.group(1)

    copy_cora_css(ros2_root)

    html_files = list(ros2_root.rglob("*.html"))
    print(f"Rethreading {len(html_files)} HTML files in {ros2_root} …")

    for f in html_files:
        process_file(f, ros2_root, version)
        print(f"  ✓  {f.relative_to(ros2_root)}")

    print(f"\nDone. {len(html_files)} files retheemed.")


if __name__ == "__main__":
    main()