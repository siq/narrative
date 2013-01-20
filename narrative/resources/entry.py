from mesh.standard import *
from scheme import *

__all__ = ('Entry',)

class Entry(Resource):
    """A logging entry."""

    name = 'entry'
    version = 1
    requests = 'create delete get query update'

    class schema:
        id = UUID(operators='equal')
        occurrence = DateTime(readonly=True, operators='gt gte lt lte')
        subject = Token(nonempty=True, operators='equal prefix in ')
        tag = Token(nonempty=True, operators='equal prefix in')
        importance = Enumeration('critical high normal low', nonnull=True,
            default='normal', operators='equal in')
        entry = Text()
        aspects = Map(Text(nonnull=True))
