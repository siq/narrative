from mesh.standard import *
from scheme import *

__all__ = ('Entry',)

class Entry(Resource):
    """A logging entry.

    Entries are primarily distinguished by their tag, expressed as a token with one or more
    colon-separated sections. The tag should indicate the overall type or category of the entry
    in a hierarchical fashion, such as "component:module:category". The tag can be filtered by
    prefix.

    Entries are further distinguished by their subject, again expressed as a token with one or
    more colon-separated sections. The subject indicates the particular application object or
    thing which this entry principally concerns.
    """

    name = 'entry'
    version = 1
    requests = 'create delete get query update'

    class schema:
        id = UUID(operators='equal')
        occurrence = DateTime(readonly=True, operators='gt gte lt lte')
        tag = Token(nonempty=True, operators='equal prefix in')
        subject = Token(nonempty=True, operators='equal prefix in')
        importance = Enumeration('critical high normal low', nonnull=True,
            default='normal', operators='equal in')
        entry = Text()
        aspects = Map(Text(nonnull=True))

    class task:
        endpoint = ('TASK', 'entry')
        title = 'Initiating an entry task'
        schema = Structure(
            structure={
                'purge-entries': {},
            },
            nonempty=True,
            polymorphic_on=Enumeration(['purge-entries'], name='task', nonempty=True))
        responses = {
            OK: Response(),
            INVALID: Response(Errors),
        }
