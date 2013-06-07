
class TokenGenerator(object):

    token_separator = ':'
    component_separator = '.'
    
    def __init__(self, component, module):
        self._component = component
        self._module = module
        self._tag_prefix = self.component_separator.join([self._component, self._module]) + self.token_separator
        return

    def get_tag(self, category):
        return self._tag_prefix + category
