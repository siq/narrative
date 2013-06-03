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
        occurrence = DateTime(readonly=True, operators='gt gte lt lte', description='The timestamp associated with this entry.')
        subject = Token(nonempty=True, operators='equal prefix in', )
        owner = UUID(operators='equal in', nonempty=True, description='ID of the user that generated this entry.')
        tag = Token(nonempty=True, operators='equal prefix in')
        importance = Enumeration('critical high normal low', nonnull=True,
            default='normal', operators='equal in')
        entry = Text()
        aspects = Map(Text(nonnull=True))

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
