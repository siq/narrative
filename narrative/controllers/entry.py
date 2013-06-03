from spire.mesh import ModelController
from spire.schema import SchemaDependency

from narrative import resources
from narrative.models import *

class EntryController(ModelController):
    resource = resources.Entry
    version = (1, 0)

    model = Entry
    schema = SchemaDependency('narrative')

    # def task(self, request, response, subject, data):
    #     session = self.schema.session

    #     task = data['task']
    #     if task == 'purge-entries':
    #         Entry.purge(session)
