from model_not_found_exception import ModelNotFoundException

class Importer:
	def __init__(self, collection):
		self.collection = collection
		self.model = False
		self.model_fields = []


	def import_note(self, import_data):
		self.__load_model(import_data['model'])

		# Create note for the relevant model and deck
		note = self.__find_or_create_note(import_data['id'])
		note.model()['did'] = self.collection.decks.id(import_data['deck']);

		# If model's first field is 'id', set its value to the node's id
		id_field = self.__get_model_id_field()
		if id_field is not None:
			note[id_field] = import_data['id']

		# Import each field
		for field in self.model_fields:
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
		self.model = model
		self.model_fields = self.collection.models.fieldNames(self.model)


	def __get_model_id_field(self):
		if len(self.model_fields) > 0 and self.model_fields[0].lower() == 'id':
			return self.model_fields[0]
		else:
			return None


	def __find_or_create_note(self, node_id):
		note = self.collection.newNote()

		id_field = self.__get_model_id_field()
		if id_field is not None:		
			existing_id = self.collection.db.scalar('select id from notes where flds LIKE ? AND mid = ?', str(node_id) +  "\x1f%", self.model['id'])
			if existing_id is not None:
				note.id = existing_id

		return note



	#def __find_card(self, node_id, model_id):
	#	note_id = this.collection.db.scalar('select id from notes where flds LIKE ? AND mid = ?', node_id +  "\x1f%", model_id)
	#	if note_id is None:
	#		return None
	#	else:
			
