S6 style presentation theme for Sphinx.

Output Sample
==============
:output: http://packages.python.org/sphinxjp.themes.s6/
:source: http://packages.python.org/sphinxjp.themes.s6/_sources/index.txt


Features
========
* provide ``s6`` directive for s6 presentation slide control.
* provide ``s6`` theme to render presentation.


Setup
=====
Make environment with ``pip``::

    $ pip install sphinxjp.themes.s6


Convert Usage
==============
setup ``conf.py`` with::

    extensions = ['sphinxjp.themes.s6']
    html_theme = 's6'

and run::

    $ make html


Writing s6 directives
=====================
Slide paging effect::

    .. s6:: effect slide

``ul`` elements move from (0,0) to (100,0) position in 5.0 secs::

    .. s6:: actions

        ['ul', 'move', '5.0', [0,0],[100,0]]

Set HTML styles on target slide::

    .. s6:: styles

        h2: {fontSize:'150%', textAlign:'center', margin:'30% auto'}

This example is a bit more complex::

    .. s6:: styles

        'ul/li': {display:'none'}

    .. s6:: actions

        ['ul/li[0]', 'fade in', '0.3'],
        ['ul/li[1]', 'fade in', '0.3'],
        ['ul/li[2]', 'fade in', '0.3'],


Requirements
============
* Python 2.5, 2.6, 2.7, 3.1, 3.2, 3.3
* Sphinx 1.2 or later is recommended.
* Sphinx < 1.2 requires sphinxjp.themecore package.


Presentation Environments
==========================
* Internet Explorer 8.0
* Firefox 3.6.x
* Chrome / Safari


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.

