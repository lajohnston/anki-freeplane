from .model_not_found_exception import ModelNotFoundException


class Importer:
    def __init__(self, collection):
        self.collection = collection
        self.model = False
        self.model_fields = []

    def import_note(self, import_data):
        self.__load_model(import_data['model'])
        note = self.__find_or_create_note(import_data['id'])
        self.__populate_note_fields(
            note, import_data['fields'], import_data['id'])

        # Set note deck
        note.model()['did'] = self.collection.decks.id(import_data['deck'])

        # Save changes
        is_new = not hasattr(note, 'mod')
        note.flush()

        # If note is new, add to collection
        if is_new:
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

    def __populate_note_fields(self, note, fields, node_id):
        # Set id field to Freeplane node id
        id_field = self.__get_model_id_field()
        if id_field is not None:
            note[id_field] = node_id

        # Populate remaining fields
        for field in self.model_fields:
            if field in fields:
                note[field] = fields[field]

    def __get_model_id_field(self):
        if len(self.model_fields) > 0 and self.model_fields[0].lower() == 'id':
            return self.model_fields[0]
        else:
            return None

    def __find_or_create_note(self, node_id):
        existing_id = self.collection.db.scalar(
            'SELECT id FROM notes WHERE flds LIKE ? AND mid = ?',
            str(node_id) + "\x1f%",
            self.model['id']
        )

        if existing_id is not None:
            note = self.collection.getNote(existing_id)
            if note is not None:
                return note

        # Existing note wasn't found
        return self.collection.newNote()
