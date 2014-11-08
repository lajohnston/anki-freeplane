class Importer:
	def __init__(self, collection):
		self.collection = collection


	def import_notes(self, notes):
		for import_data in notes:
			self.__set_deck(import_data['deck'])
			model = self.__set_model(import_data['model'])

			note = self.collection.newNote()
			field_names = self.collection.models.fieldNames(model)

			# If model's first field is 'id', set its value to the node's id
			if len(field_names) > 0 and field_names[0].lower() == 'id':
				note[field_names[0]] = import_data['id']

			# Import each field
			for field in field_names:
				if field in import_data['fields']:
					note[field] = import_data['fields'][field]


	def __set_deck(self, deck_name):
		deck_id = self.collection.decks.id(deck_name)
		self.collection.decks.select(deck_id)


	def __set_model(self, model_name):
		model = self.collection.models.byName(model_name)
		self.collection.models.setCurrent(model)
		return model




	#mw.col.models.fieldNames(model)


#Import a text file into the collection

	#from anki.importing import TextImporter
	#file = u"/path/to/text.txt"
	# select deck
	#did = mw.col.decks.id("ImportDeck")
	#mw.col.decks.select(did)
	# set note type for deck
	#m = mw.col.models.byName("Basic")
	#deck = mw.col.decks.get(did)
	#deck['mid'] = m['id']
	#mw.col.decks.save(deck)
	# import into the collection
	#ti = TextImporter(mw.col, file)
	#ti.initMapping()
	#ti.run()


