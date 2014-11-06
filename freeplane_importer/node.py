import re

class Node:
	def __init__(self, doc, element):
		self.doc = doc
		self.element = element
		self.fields = False
		self.children = False


	def to_dict(self):
		return {
			'id': self.get_node_id(),
			'deck': self.get_deck(),
			'model': self.get_model(),
			'fields': self.get_fields()
		}

	def get_node_id(self):
		return self.element.get('ID')

	def get_model(self):
		return self.get_attribute('anki:model')

	def get_deck(self):
		current = self.element
		
		# Check for anki:deck value, traversing ancestor nodes until one is found
		while True:
			deck = current.find('attribute[@NAME="anki:deck"]')
			if deck is not None:
				return deck.get('VALUE')

			# Traverse to parent - ElementTree doesn't support get parent, so have to search from root
			current = self.doc.find('.//node[@ID="' + current.get('ID') + '"]/..')

			if current is None or current.tag != 'node':
				return None


	##
	# Returns a dict of field : value pairs for the given mindmap node
	##
	def get_fields(self, fields = {}):
		if self.fields is False:
			fields = self.__parse_main_field(fields)
			for child in self.get_children():
				fields = child.get_fields(fields)
			self.fields = fields

		return self.fields
		


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
	def __parse_main_field(self, fields):
		name = self.get_attribute('anki:field')
		if name is not None:
			field_value = self.element.get('TEXT')
			
			# Apply modification defined in anki:modify field
			modifier = self.get_attribute('anki:modify')
			if modifier is not None:
				field_value = re.sub(r'(?<!\\)\*', field_value, modifier)

			fields[name] = field_value
		
		return fields


	def get_attribute(self, name):
		attribute = self.element.find('attribute[@NAME="' + name + '"]')
		if attribute is None:
			return None
		else:
			return attribute.get('VALUE')


	def defines_own_field(self):
		return self.get_attribute('anki:field') is not None


	def get_children(self):
		if self.children is False:
			children = []
			for child_element in self.element.findall('./node'):
				# If sub-node isn't its own note/model
				if child_element.find('attribute[@NAME="anki:model"]') is None:
					children.append(Node(self.doc, child_element))
			self.children = children

		return self.children


	def get_text(self):
		return self.element.get('TEXT')
