import xml.etree.ElementTree as etree

class XMLConnector(object):
    def __init__(self,filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
