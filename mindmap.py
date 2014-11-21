import os

from aqt import mw # import the main window object (mw) from ankiqt
from aqt.utils import showInfo # import the "show info" tool from utils.py
from aqt.qt import * # import all of the Qt GUI library

from freeplane_importer.model_not_found_exception import ModelNotFoundException
from xml.etree.ElementTree import ElementTree
from freeplane_importer.reader import Reader
from freeplane_importer.importer import Importer

##
# Entry point for the anki plugin
##
def importMindmap():
	# Load freeplane example mindmap xml
	doc = ElementTree()
	doc.parse(os.path.dirname(__file__) + '/example/ExampleMindmap.mm')
	
	# Extract notes from xml
	reader = Reader()
	notes = reader.get_notes(doc)

	# Import notes into Anki
	importer = Importer(mw.col)
	for note in notes:
		try:
			importer.import_note(note)
		except ModelNotFoundException as e:
			showInfo('Model ' + e.model_name + ' not found')

	mw.reset()

# Create a new menu item and add it to the tools menu
action = QAction("Import mindmap", mw)
mw.connect(action, SIGNAL("triggered()"), importMindmap)
mw.form.menuTools.addAction(action)
