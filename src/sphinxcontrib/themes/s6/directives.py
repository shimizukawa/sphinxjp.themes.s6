# -*- coding: utf-8 -*-
from docutils import nodes

from sphinx.locale import _
from sphinx.environment import NoUri
from sphinx.util.compat import Directive, make_admonition

class s6_node(nodes.raw): pass


class S6(Directive):
    """
    A s6 entry, control s6 slide effects, actions and styles.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        event = self.arguments[0]
        if len(self.arguments) == 2:
            contents = self.arguments[1]
        else:
            contents = '\n'.join(self.content)

        if event == 'effect':
            if contents not in ('slide', 'fade', 'fadeScale', 'fadeScaleFromUp', 'fadeScaleFromUpTransparent'):
                raise RuntimeError('Unknown effect type: %r' % contents)
            contents = "'%s'" % contents
        elif event == 'actions':
            contents = "[%s]" % contents.strip().strip(',')
        elif event == 'styles':
            contents = "{%s}" % contents.strip().strip(',')
        else:
            raise RuntimeError('Unknown event name: %r' % event)

        text = """if(typeof s6 != 'undefined'){s6.page({%s: %s});}""" % (event, contents)
        node = s6_node(text)

        if 'class' in self.options:
            node['classes'] += options['class']

        return [node]


def process_s6s(app, doctree):
    # collect all s6s in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 's6_all_s6s'):
        env.s6_all_s6s = []
    for node in doctree.traverse(s6_node):
        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        env.s6_all_s6s.append({
            'docname': env.docname,
            'lineno': node.line,
            's6': node.deepcopy(),
            'target': targetnode,
        })


def purge_s6s(app, env, docname):
    if not hasattr(env, 's6_all_s6s'):
        return
    env.s6_all_s6s = [s6 for s6 in env.s6_all_s6s
                      if s6['docname'] != docname]


def visit_s6_node(self, node):
    self.body.append(self.starttag(node, 'script'))
    self.body.append(node.rawsource)
    self.set_first_last(node)

def depart_s6_node(self, node=None):
    self.body.append('</script>\n')

def setup(app):
    app.add_config_value('s6_include_s6s', False, False)

    app.add_node(s6_node, html=(visit_s6_node, depart_s6_node))

    app.add_directive('s6', S6)
    app.connect('doctree-read', process_s6s)
    app.connect('env-purge-doc', purge_s6s)


