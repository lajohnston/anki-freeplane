 
 # READ : 
 # https://docs.python.org/2/library/xml.etree.elementtree.html#example


#import xpath
#context = xpath.XPathContext()

#from xml.parsers import expat

from freeplane_node import FreeplaneNode

class FreeplaneReader:
	##
	# Returns an array of notes. Each note is a dict object with the
	# following keys:
	#  
	# deck		the name of the deck the note belongs in
	# model		the model (note type) of the note
	# fields	field: value pairs of all fields in the note
	# id		the id of the node in the mindmap
	##
	def parse_notes(self, doc):
		self.doc = doc
		self.note_nodes = doc.findall('.//attribute[@NAME="anki:model"]/..')

		notes = []
		for element in self.note_nodes:
			node = FreeplaneNode(doc, element)

			note = node.to_dict()
			if note is not None:
				notes.append(note)
			
			print note

		return notes
