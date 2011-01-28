# -*- coding: utf-8 -*-

from os import path
import directives
from sphinx.theming import Theme

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates')


def setup_s6_theme(app):
    theme = app.config._raw_config.get('s6_theme', 'default')
    #app.add_config_value('s6_theme', theme, True)

    if 's6' in Theme.themes:
        return
    Theme.themes['s6'] = (path.join(template_path, theme), None)


def setup(app):
    directives.setup(app)
    setup_s6_theme(app)
