import unittest
from freeplane_importer.importer import Importer
from mock import Mock
from mock import call


class TestImporter(unittest.TestCase):

	def setUp(self):
		self.mock_collection = Mock()
		
		self.fake_model = {'id': 1}
		self.mock_collection.models.byName.return_value = self.fake_model

		self.fake_deck = {}
		self.mock_collection.decks.get.return_value = self.fake_deck

		self.fake_note = {}
		self.mock_collection.newNote.return_value = self.fake_note

		self.mock_collection.models.fieldNames.return_value = []

		self.importer = Importer(self.mock_collection)

		self.notes = [
			{
				'id': 100,			
				'deck': 'History',
				'model': 'Basic',
				'fields': {}
			}			
		]


	def test_it_should_select_the_deck_for_each_note(self):
		self.mock_collection.decks.id.return_value = 1000

		self.importer.import_notes(self.notes)
		self.mock_collection.decks.id.assert_called_with('History')
		self.mock_collection.decks.select.assert_called_with(1000)


	def test_it_should_find_the_model_for_each_note(self):
		self.importer.import_notes(self.notes)
		self.mock_collection.models.byName.assert_called_with('Basic')


	def test_it_should_set_the_correct_model_in_the_collection(self):
		# Set up fake model with a fake id
		fake_model = {'id': 100}
		self.mock_collection.models.byName.return_value = fake_model

		self.importer.import_notes(self.notes)
		self.mock_collection.models.setCurrent.assert_called_with(fake_model)	


	def test_it_should_create_a_new_note(self):
		self.importer.import_notes(self.notes)
		self.mock_collection.newNote.assert_called_with()


	def test_it_should_get_the_field_names_from_the_model(self):
		self.importer.import_notes(self.notes)
		self.mock_collection.models.fieldNames.assert_called_with(self.fake_model)


	def test_it_should_save_the_node_id_if_the_first_field_is_named_id_in_lowercase(self):
		self.mock_collection.models.fieldNames.return_value = ['id']
		self.importer.import_notes(self.notes)

		self.assertEqual(100, self.fake_note['id'])


	def test_it_should_save_the_node_id_if_the_first_field_is_named_id_in_uppercase(self):
		self.mock_collection.models.fieldNames.return_value = ['ID']
		self.importer.import_notes(self.notes)

		self.assertEqual(100, self.fake_note['ID'])


	def test_it_should_populate_the_note_with_the_field_values(self):
		self.notes[0]['fields'] = {
			'Front' : 'Front value',
			'Back' : 'Back value'
		}

		self.mock_collection.models.fieldNames.return_value = ['Front', 'Back']
		self.importer.import_notes(self.notes)
		self.assertEqual('Front value', self.fake_note['Front'])
		self.assertEqual('Back value', self.fake_note['Back'])


	def test_it_should_ignore_fields_that_do_not_exist_in_the_model(self):
		self.notes[0]['fields'] = {
			'Front' : 'Front value',
			'Back' : 'Back value'
		}

		self.mock_collection.models.fieldNames.return_value = ['Front']
		self.importer.import_notes(self.notes)
		self.assertFalse('Back' in self.fake_note)
