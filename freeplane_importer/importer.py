class Importer:
	def __init__(self, collection):
		self.collection = collection


	def import_notes(self, notes):
		for import_data in notes:
			model = self.__set_deck_model(import_data['deck'], import_data['model'])

			note = self.collection.newNote()
			field_names = self.collection.models.fieldNames(model)

			# If model's first field is 'id', set its value to the node's id
			if len(field_names) > 0 and field_names[0].lower() == 'id':
				note[field_names[0]] = import_data['id']

			# Import each field
			for field in field_names:
				if field in import_data['fields']:
					note[field] = import_data['fields'][field]

			if note.dupeOrEmpty() != 2:
				self.collection.addNote(note)


	def __set_deck_model(self, deck_name, model_name):
		# select deck
		did = self.collection.decks.id(deck_name)
		self.collection.decks.select(did)
		
		# set note type for deck
		m = self.collection.models.byName(model_name)
		deck = self.collection.decks.get(did)
		deck['mid'] = m['id']
		self.collection.decks.save(deck)

		return m
