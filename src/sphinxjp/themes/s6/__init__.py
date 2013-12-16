# -*- coding: utf-8 -*-

from os import path

import sphinx
from sphinx.application import ExtensionError

from sphinxjp.themes.s6 import directives


IS_SUPPORTED_THEMEPLUGIN = getattr(sphinx, 'version_info', (1, 1))[:2] >= (1, 2)
try:
    from sphinxjp.themecore import setup_themes
except ImportError:
    setup_themes = None

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates')


def get_path():
    """entry-point for sphinxjp.themecore theme."""
    return template_path


def on_doctree_resolved(self, doctree, docname):
    if self.builder.name in ('singlehtml', 'html'):
        return

    for node in doctree.traverse(directives.s6_node):
        node.parent.remove(node)


def setup(app):
    """entry-point for sphinx"""
    if IS_SUPPORTED_THEMEPLUGIN:
        pass
    elif setup_themes is not None:
        setup_themes(app)
    else:
        raise ExtensionError(
            'sphinxjp.themes.s6 requires at least Sphinx-1.2 or '
            'Sphinx-1.1 + sphinxjp.themecore to run.'
        )

    directives.setup(app)
    app.connect("doctree-resolved", on_doctree_resolved)
    app.add_javascript('jquery.touchwipe.min.js')
    app.add_javascript('s6.js')
    app.add_javascript('s6-sphinx.js')
