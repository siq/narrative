'''
Created on Feb 3, 2015

@author: nirmal
'''

from mesh.standard import *
from scheme import *

__all__ = ('Notification',)

class Notification(Resource):
    """A resource Notification."""

    name = 'notification'
    version = 1
    requests = 'create put query'

 
    class schema:
        id = UUID(operators='equal', oncreate=True)
        status = Enumeration('read unread', nullable=True, default='unread')
        resource = Surrogate(nullable=False)
        ownerID = UUID(operators='equal')
        type = Token(nullable=False)
        entity = Token(nullable=False)
        created = DateTime(utc=True, sortable=True)
        
    
    class markallread:
        endpoint = ('MARKALLREAD', 'notification')
        title = 'Update multiple notifications from unread to read'
        schema = Structure({
            'notification_ids': Sequence(UUID(nonnull=True, description='set of uuid of notification.')),
        }, nonempty=True)
        responses = {
            OK: Response(),
            INVALID: Response(Errors),
        }
        
    class task:
        endpoint = ('TASK', 'notification')
        title = 'Initiating a notification task'
        schema = Structure(
            structure={
                'purge-notifications': {},
            },
            polymorphic_on='task',
            nonempty=True)
        responses = {
            OK: Response(),
            INVALID: Response(Errors),
        }