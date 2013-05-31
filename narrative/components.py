from datetime import datetime

from mesh.standard import bind
from spire.core import Component
from spire.exceptions import TemporaryStartupError
from spire.mesh import MeshDependency, MeshServer
from spire.runtime import onstartup

from narrative import models
from narrative.bindings import platoon
from narrative.bundles import API

RecurringTask = bind(platoon, 'platoon/1.0/recurringtask')
Schedule = bind(platoon, 'platoon/1.0/schedule')

DAILY = Schedule(
    id='4278895b-3b8e-4ba9-9e3c-b21c5fec58b8',
    name='daily at 2am',
    schedule='fixed',
    anchor=datetime(2000, 1, 1, 2, 0, 0),
    interval=86400)

PURGE_ENTRIES = RecurringTask(
    id='426eb30a-96e2-4383-b050-3b80715fe6d1',
    tag='purge-entries',
    schedule_id=DAILY.id,
    retry_limit=0)

class Narrative(Component):
    api = MeshServer.deploy(bundles=[API], path='/')

    narrative = MeshDependency('narrative')
    platoon = MeshDependency('platoon')

    @onstartup(service='narrative')
    def startup_narrative(self):
        DAILY.put()
        PURGE_ENTRIES.set_http_task(
            self.narrative.prepare('narrative/1.0/entry', 'task', None,
            {'task': 'purge-entries'}))
        PURGE_ENTRIES.put()
