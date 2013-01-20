from spire.core import Component
from spire.mesh import MeshServer

from narrative import models
from narrative.bundles import API

class Narrative(Component):
    api = MeshServer.deploy(bundles=[API], path='/')
