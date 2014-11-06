# import the main window object (mw) from ankiqt
#from aqt import mw
# import the "show info" tool from utils.py
#from aqt.utils import showInfo
# import all of the Qt GUI library
#from aqt.qt import *


import os

from xml.etree.ElementTree import ElementTree
from freeplane_importer import Reader


Reader()

def importMindmap():
	# Load freeplane mindmap xml
	doc = ElementTree()

	
	doc.parse(os.path.dirname(__file__) + '/example/ExampleMindmap.mm')
	
	# Extract notes from xml
	reader = Reader()
	notes = reader.parse_notes(doc)

	# Import notes into Anki
	importer = Importer()
	importer.import_notes(notes)


# Create a new menu item and add it to the tools menu
action = QAction("Import mindmap", mw)
mw.connect(action, SIGNAL("triggered()"), importMindmap)
mw.form.menuTools.addAction(action)

