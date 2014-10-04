 
 # READ : 
 # https://docs.python.org/2/library/xml.etree.elementtree.html#example


#import xpath
#context = xpath.XPathContext()

#from xml.parsers import expat

import re

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
			deck = self.__get_note_deck(element)
			if deck is None:
				continue

			note = {
				'id': element.get('ID'),
				'deck': deck,
				'model': self.__get_attribute(element, 'anki:model'),
				'fields': self.__get_note_fields(element)
			}

			notes.append(note)
			print note

		return notes


	def __get_note_deck(self, element):
		# Check for anki:deck value, traversing ancestor nodes until one is found
		current = element

		while True:
			deck = self.__get_attribute(current, 'anki:deck')
			if deck is not None:
				return deck

			# Traverse to parent - ElementTree doesn't support get parent, so have to search from root
			current = self.doc.find('.//node[@ID="' + current.get('ID') + '"]/..')
			if current is None or current.tag != 'node':
				return None


	##
	# Returns a dict of field : value pairs for the given mindmap node
	##
	def __get_note_fields(self, element):
		fields = {}
		self.__get_main_field(element, fields)

		return fields

		#if main_field is not None:
		#	fields[main_field.get('VALUE')] = self.__get_note_element_main_field_value(element)

			#fields[main_field]


	##
	# Returns a dict containing the field_name : value pair for this mindmap node's
	# 'main' field, that is, the field defined in the anki:field attribute. The field
	# value is modified by the anki:modify template, which can define a template
	# containing a '*' character that is replaced by the node's text.
    #
	# A template without a '*' character is a way of ignoring the node text completely
	# and defining a custom value. A * character can be escaped with a preceding \,
	# in which case it is output as-is
	##
	def __get_main_field(self, element, fields):
		name = self.__get_attribute(element, 'anki:field')
		if name is not None:
			field_value = element.get('TEXT')
			
			# Apply modification defined in anki:modify field
			modifier = self.__get_attribute(element, 'anki:modify')
			if modifier is not None:
				field_value = re.sub(r'(?<!\\)\*', field_value, modifier)

			fields[name] = field_value


	def __get_attribute(self, element, name):
		attribute = element.find('attribute[@NAME="' + name + '"]')
		if attribute is None:
			return None
		else:
			return attribute.get('VALUE')


	##
	# Returns a dict containing a field : value pair for the node's anki:content attribute.
	# The field name is defined in the attribute, and the children and derived from all its
	# child nodes that do not define fields of their own
	##
	#def __get_content_field(self, element):
		#if element.get

	##
	#
	##
	def __get_child_fields(self, element, fields):
		for node in element.findall('node'):
			self.__get_main_field(element, fields)




