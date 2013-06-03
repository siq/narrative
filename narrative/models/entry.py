from scheme import current_timestamp
from spire.schema import *

__all__ = ('Entry',)

schema = Schema('narrative')

class Entry(Model):
    """An entry."""

    class meta:
        schema = schema
        tablename = 'entry'

    id = Identifier()
    occurrence = DateTime(timezone=True, nullable=False, default=current_timestamp)
    subject = Token(nullable=False, index=True)
    owner = Text(nullable=False, index=True)
    tag = Token(nullable=False, index=True)
    importance = Enumeration('critical high normal low', nullable=False, default='normal')
    entry = Text()
    aspects = Hstore()

    # @classmethod
    # def purge(cls, session):
    #     pass

EntryAspectsIndex = Index('entry_aspects_idx', Entry.aspects, postgresql_using='gist')
EntryOwnerIndex = Index('entry_owner_idx', Entry.owner)
