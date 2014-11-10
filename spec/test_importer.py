import unittest
from freeplane_importer.importer import Importer
from mock import Mock
from mock import MagicMock
from mock import call

from freeplane_importer.model_not_found_exception import ModelNotFoundException


class TestImporter(unittest.TestCase):

	def setUp(self):
		self.mock_collection = Mock()
		
		self.fake_model = {'id': 1}
		self.mock_collection.models.byName.return_value = self.fake_model

		self.fake_deck = {}
		self.mock_collection.decks.get.return_value = self.fake_deck

		self.mock_note = MagicMock()
		self.mock_collection.newNote.return_value = self.mock_note

		self.mock_collection.models.fieldNames.return_value = []

		self.importer = Importer(self.mock_collection)

		self.note = {
			'id': 100,			
			'deck': 'History',
			'model': 'Basic',
			'fields': {}
		}	


	def test_it_should_select_the_deck_for_each_note(self):
		self.mock_collection.decks.id.return_value = 1000

		self.importer.import_note(self.note)
		self.mock_collection.decks.id.assert_called_with('History')
		self.mock_collection.decks.select.assert_called_with(1000)


	def test_it_should_find_the_model_for_each_note(self):
		self.importer.import_note(self.note)
		self.mock_collection.models.byName.assert_called_with('Basic')

	#def test_it_should_set_the_correct_model_in_the_collection(self):
		# Set up fake model with a fake id
	#	fake_model = {'id': 100}
	#	self.mock_collection.models.byName.return_value = fake_model

	#	self.importer.import_note(self.note)
	#	self.mock_collection.models.setCurrent.assert_called_with(fake_model)	


	#def test_it_should_generate_a_new_model_from_the_fields_if_the_model_does_not_exist(self):
	#	self.mock_collection.models.byName.return_value = None
	#	new_model = {
	#		'name': 'Basic',
	#		'flds': []
	#	}

	#	self.mock_collection.models.new.return_value = new_model


	#	self.importer.import_note(self.note)
	#	self.mock_collection.models.new.assert_called_with('Basic')
	#	new_model.
	
	def test_it_should_return_true_if_note_was_added_successfully(self):
		self.assertTrue(self.importer.import_note(self.note))



	def test_it_should_raise_a_no_model_exception_if_the_model_does_not_exist(self):
		self.mock_collection.models.byName.return_value = None
		self.assertRaises(ModelNotFoundException, self.importer.import_note, self.note);



	def test_it_should_create_a_new_note(self):
		self.importer.import_note(self.note)
		self.mock_collection.newNote.assert_called_with()


	def test_it_should_get_the_field_names_from_the_model(self):
		self.importer.import_note(self.note)
		self.mock_collection.models.fieldNames.assert_called_with(self.fake_model)


	def test_it_should_save_the_node_id_if_the_first_field_is_named_id_in_lowercase(self):
		self.mock_collection.models.fieldNames.return_value = ['id']
		self.importer.import_note(self.note)

		self.mock_note.__setitem__.assert_called_with('id', 100)


	def test_it_should_save_the_node_id_if_the_first_field_is_named_id_in_uppercase(self):
		self.mock_collection.models.fieldNames.return_value = ['ID']
		self.importer.import_note(self.note)

		self.mock_note.__setitem__.assert_called_with('ID', 100)


	def test_it_should_populate_the_note_with_the_field_values(self):
		self.note['fields'] = {
			'Front' : 'Front value',
			'Back' : 'Back value'
		}

		self.mock_collection.models.fieldNames.return_value = ['Front', 'Back']
		self.importer.import_note(self.note)

		self.mock_note.__setitem__.assert_has_calls([call('Front', 'Front value'), call('Back', 'Back value')])


	def test_it_should_ignore_fields_that_do_not_exist_in_the_model(self):
		self.note['fields'] = {
			'Front' : 'Front value',
			'Back' : 'Back value'
		}

		self.mock_collection.models.fieldNames.return_value = ['Front']
		self.importer.import_note(self.note)
		self.assertFalse('Back' in self.mock_note)
