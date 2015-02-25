'''
Created on Feb 4, 2015

@author: nirmal
'''
from mesh.standard import bind
from mesh.testing import MeshTestCase
from spire.core import Unit
from spire.mesh import MeshDependency
from spire.runtime.testing import Runtime
import unittest
from enamel.bundles import API
from spire.core import adhoc_configure, Unit
from scheme import Format, Structure, Token
from scheme.surrogate import surrogate

adhoc_configure({
    'schema:enamel': {
        'url': 'postgresql://postgres@localhost/enamel',
    },
    'schema:docket': {
        'url': 'postgresql://postgres@localhost/docket',
    },
    'schema:flux': {
        'url': 'postgresql://postgres@localhost/flux',
    },
    'mesh:enamel': {
        'url': 'http://localhost:9999/api.enamel',
        'bundle': 'enamel.API'
    },
    'mesh:narrative': {
        'url': 'http://localhost:9993/',
        'bundle': 'narrative.API'
    },
    'mesh:docket': {
        'url': 'http://localhost:9998/',
        'bundle': 'docket.API',
    },
    'mesh:docket.entity': {
        'url': 'http://localhost:9998/',
        'introspect': True,
    },
    'mesh:tidings': {
         'bundle': 'tidings.API',
         'url': 'http://localhost:9996/api',
    },
})

class TestDependency(Unit):
    enamel = MeshDependency('enamel')
    docket_entity = MeshDependency('docket.entity')
    narrative = MeshDependency('narrative')
     
class TestNotification(MeshTestCase):
    bundle = API
    maxDiff = None
    config = TestDependency()

class TestUserNotifications(TestNotification):
    bundle = API

    enamel = MeshDependency('enamel')
    
         
    def test_notification_query(self):
            owner_id_ = '2533dc9a-0fbe-4ab7-bd10-a65e2ec07cfc'
            notification = self.config.narrative.bind('narrative/1.0/notification')
            res_ = notification.query(sort=['created-']).filter(ownerID=owner_id_).all()
            print res_[0].__dict__
            data = {'notification_ids' :['a96be911-dd4a-4905-9cbd-a71fdbee60ee','e6c68874-e6a5-47f6-b0e1-510b7d89f0dd']}
            res_ = notification._get_client().execute('narrative/1.0/notification', 'markallread', None, data)
            print res_
            data={'total':True,'query':{'ownerID':owner_id_,'status':'unread'}}
            res_ = notification._get_client().execute('narrative/1.0/notification', 'query', None, data)
            print res_.content['total']
       
def makeSuite():
    return unittest.defaultTestLoader.loadTestsFromTestCase(TestUserNotifications)

if __name__ == "__main__":
    unittest.TextTestRunner().run(makeSuite())