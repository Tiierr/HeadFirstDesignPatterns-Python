from JSONConnector import JSONConnector
from XMLConnector import XMLConnector

class Factory(object):
    def __init__(self,filepath):
        self.filepath = filepath

    def connection_factory(self):
        if self.filepath.endswith('json'):
            connector = JSONConnector(self.filepath)
        elif self.filepath.endswith('xml'):
            connector = XMLConnector(self.filepath)
        else:
            raise ValueError('Cannot connect to {}'.format(self.filepath))
        return connector

    def connect_to(self):
        factory = None
        try:
            factory = self.connection_factory()
        except ValueError as ve:
            print(ve)
        return factory

    def getFactory(self):
        return self.connect_to()
