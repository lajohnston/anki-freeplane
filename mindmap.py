from freeplane_importer import FreeplaneReader
from xml.etree.ElementTree import ElementTree

doc = ElementTree()
doc.parse('../../../Dropbox/Anki deck mindmap.mm')

reader = FreeplaneReader()
notes = reader.parse_notes(doc)

