from model_not_found_exception import ModelNotFoundException

class Importer:
	def __init__(self, collection):
		self.collection = collection


	def import_note(self, import_data):
		# Create note for the relevant model and deck
		model = self.__load_model(import_data['model'])
		note = self.collection.newNote()
		note.model()['did'] = self.collection.decks.id(import_data['deck']);

		# If model's first field is 'id', set its value to the node's id
		field_names = self.collection.models.fieldNames(model)
		if len(field_names) > 0 and field_names[0].lower() == 'id':
			note[field_names[0]] = import_data['id']

		# Import each field
		for field in field_names:
			if field in import_data['fields']:
				note[field] = import_data['fields'][field]

		if note.dupeOrEmpty() != 2:
			self.collection.addNote(note)

		return True


	def __load_model(self, model_name):
		# Get model
		model = self.collection.models.byName(model_name)
		if model is None:
			raise ModelNotFoundException(model_name)

		# Set current model
		self.collection.models.setCurrent(model)

		return model