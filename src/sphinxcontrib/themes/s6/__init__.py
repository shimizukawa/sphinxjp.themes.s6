# -*- coding: utf-8 -*-

from os import path
import directives
from sphinx.theming import Theme

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates')


def get_path():
    """entry-point for sphinxcontrib-theme-core theme."""
    return template_path


def setup_directives(app):
    """entry-point for sphinxcontrib-theme-core directive."""
    directives.setup(app)


def setup_s6_theme(app):
    theme = app.config._raw_config.get('s6_theme', 'default')
    if theme == 'default':
        theme = 's6'
    #app.add_config_value('s6_theme', theme, True)

    if 's6' in Theme.themes:
        return
    Theme.themes['s6'] = (path.join(template_path, theme), None)


def setup(app):
    """ setup entry point for sphinx conf.py """
    setup_directives(app)
    setup_s6_theme(app)
