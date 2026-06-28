"""Sphinx configuration for CORA documentation."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

sys.path.insert(0, str(REPO_ROOT / "codi" / "src" / "codi"))

project   = "CORA"
copyright = "2024, CORA Project Team"
author    = "CORA Project Team"
version   = "0.1"
release   = "0.1-alpha"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "myst_parser",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "attrs_inline",
    "html_image",
]
myst_heading_anchors = 3

autodoc_default_options = {
    "members":         True,
    "undoc-members":   False,
    "private-members": False,
    "special-members": "__init__",
    "show-inheritance": True,
    "member-order":    "bysource",
}
autodoc_typehints                     = "description"
autodoc_typehints_description_target  = "documented"
autodoc_class_signature               = "separated"
add_module_names                      = False

napoleon_google_docstring             = True
napoleon_numpy_docstring              = False
napoleon_include_init_with_doc        = True
napoleon_use_admonition_for_notes     = True
napoleon_use_admonition_for_examples  = True
napoleon_use_rtype                    = False

autosummary_generate           = True
autosummary_generate_overwrite = True
autosummary_imported_members   = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md":  "markdown",
}
master_doc = "index"
language   = "en"
exclude_patterns = [
    "_build",
    "docs_build",
    "api/ros2/docs_build",
    "Thumbs.db",
    ".DS_Store",
    "_theme",
    "**.ipynb_checkpoints",
    "cross_reference",
]

html_theme      = "cora"
html_theme_path = ["_theme"]
html_title       = "CORA Documentation"
html_short_title = "CORA Docs"
html_allow_unsafe_html = True  # needed for raw:: html redirect blocks

html_context = {
    "github_url": "https://github.com/your-org/cora",
    "version":    release,
    "toctree_sections": [],
}

html_static_path     = ["_static"]
html_use_index       = True
html_show_sphinx     = False
html_show_copyright  = True
html_copy_source     = False
html_show_sourcelink = False

pygments_style     = "monokai"
todo_include_todos = True


def setup(app):
    from docutils import nodes
    from sphinx.util.docutils import SphinxRole

    class RosRole(SphinxRole):
        def run(self):
            pkg  = self.text
            url  = f"../api/ros2/{pkg}/{pkg}/index.html"
            node = nodes.reference(pkg, pkg, internal=False, refuri=url)
            return [node], []

    app.add_role("ros", RosRole())
