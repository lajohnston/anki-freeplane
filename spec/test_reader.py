import unittest
from freeplane_importer.reader import Reader
from mock import Mock


class TestReader(unittest.TestCase):

    def setUp(self):
        self.reader = Reader()
        self.mock_doc = Mock()
        self.mock_doc.findall.return_value = []

    def test_it_should_find_all_elements_in_the_document_with_an_anki_model_attribute(self):
        self.reader.get_notes(self.mock_doc)
        self.mock_doc.findall.assert_called_with(
            './/attribute[@NAME="anki:model"]/..')

    def test_it_should_return_an_array_of_notes(self):
        result = self.reader.get_notes(self.mock_doc)
        self.assertTrue(isinstance(result, list))
