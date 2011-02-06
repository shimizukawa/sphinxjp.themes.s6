# -*- coding: utf-8 -*-

from os import path
import directives

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates')


def get_path():
    """entry-point for sphinxcontrib-theme-core theme."""
    return template_path


def setup_directives(app):
    """entry-point for sphinxcontrib-theme-core directive."""
    directives.setup(app)
