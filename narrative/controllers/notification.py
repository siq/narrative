'''
Created on Feb 4, 2015

@author: nirmal
'''
from spire.mesh import ModelController
from spire.schema import *
from narrative.resources.notification import Notification as NotificationResource
from narrative.models.notification import Notification
from spire.schema import SchemaDependency
from sqlalchemy.exc import IntegrityError
from scheme import current_timestamp
from datetime import timedelta
import json


    
class NotificationController(ModelController):
    resource = NotificationResource
    version = (1, 0)
    model = Notification
    schema = SchemaDependency('narrative')
    
    mapping = {
        'id': 'id',
        'created': 'created',
        'status': 'status',
        'resource': 'resource',
        'ownerID': 'ownerid',
        'type': 'type',
        'entity': 'entity',
    }
    
    
    def markallread(self, request, response, subject, data):
        try:
            session = self.schema.session
            session.query(self.model).filter(self.model.id.in_(data['notification_ids'])).update({self.model.status:'read'}, synchronize_session=False)       
            session.commit()
        except IntegrityError, e:
            raise ValidationError({'token': 'data-integrity-error',
            'message': 'Notification is not updated in table.'})
    
    def task(self, request, response, subject, data):
        session = self.schema.session
        delta = current_timestamp() - timedelta(days=2)
        if data['task'] == 'purge-notifications':
            session.query(Notification).filter(Notification.created < delta).delete(synchronize_session=False)
        session.commit()
        
    def query(self, request, response, subject, data):
        query = self.schema.session.query(self.model)
        filters = data.get('query')
        if filters:
            query = self._construct_filters(query, filters)
        query = self._annotate_query(request, query, data)
        total = query.count()
        if data.get('total'):
            return response({'total': total})
        if 'sort' in data:
            query = self._construct_sorting(query, data['sort'])
        if 'limit' in data:
            query = query.limit(data['limit'])
        if 'offset' in data:
            query = query.offset(data['offset'])
        resources = []
        for instance in query.all():
            resources.append(self._construct_resource(request, instance, data))
        response({'total': total, 'resources': resources})