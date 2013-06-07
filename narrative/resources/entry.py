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
        occurrence = DateTime(readonly=True, operators='gt gte lt lte', description='The timestamp associated with this entry.')
        subject = Token(nonempty=True, operators='equal prefix in', description='The subject of the action being logged - normally just a UUID.')
        owner = UUID(operators='equal in', nonempty=True, description='ID of the user that generated this entry.')
        tag = Token(nonempty=True, operators='equal prefix in', description='A hierarchical field defining the application component that generates this entry.')
        importance = Enumeration('critical high normal low', nonnull=True,
            default='normal', operators='equal in', description='Importance level attached to the entry.')
        entry = Text(description='Free-form field describing the entry in more detail.')
        aspects = Map(Text(nonnull=True), description='A map to hold other information in the form of adhoc name-value pairs.')

    # class task:
    #     endpoint = ('TASK', 'entry')
    #     title = 'Initiating an entry task'
    #     schema = Structure(
    #         structure={
    #             'purge-entries': {},
    #         },
    #         nonempty=True,
    #         polymorphic_on=Enumeration(['purge-entries'], name='task', nonempty=True))
    #     responses = {
    #         OK: Response(),
    #         INVALID: Response(Errors),
    #     }
