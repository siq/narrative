'''
Created on Feb 4, 2015

@author: nirmal
'''
from scheme import current_timestamp
from spire.schema import *
from spire.mesh import Surrogate

__all__ = ('Notification',)

schema = Schema('narrative')

class Notification(Model):
    """A notification."""

    class meta:
        schema = schema
        tablename = 'notification'

    id = Identifier()
    created = DateTime(timezone=True, nullable=False, default=current_timestamp)
    read = Boolean(default=False)
    resource = Surrogate(nullable=False)
    ownerid = Token(nullable=True, index=True)
    type = Token(nullable=False)
    entity = Token(nullable=False)
    
NotificationOwnerIDIndex = Index('notification_ownerid_idx', Notification.ownerid)
NotificationReadIndex = Index('notification_read_idx', Notification.read)
