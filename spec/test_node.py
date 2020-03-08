import unittest
from freeplane_importer.node import Node

from xml.etree.ElementTree import ElementTree
from xml.etree import ElementTree as etree


class TestNode(unittest.TestCase):

    def setUp(self):
        self.root = etree.fromstring("<map></map>")
        self.next_id = 0

    def __add_node(self, parent, attributes={}, text=''):
        self.next_id += 1
        string = '<node TEXT="' + text + '" ID="ID_' + str(self.next_id) + '">'

        for name, value in attributes.items():
            string += '<attribute NAME="' + name + '" VALUE="' + value + '"/>'

        string += '</node>'
        node = etree.fromstring(string)
        parent.append(node)
        return node

    def test_it_should_extract_the_deck_from_the_nearest_ancestor_of_the_node(self):
        node1 = self.__add_node(self.root, {'anki:deck': 'root_deck'})
        node2 = self.__add_node(node1, {'anki:deck': 'parent_deck'})
        node3 = self.__add_node(node2)
        fp_node = Node(self.root, node3)

        self.assertEqual('parent_deck', fp_node.get_deck())

    def test_it_should_extract_the_model_from_the_anki_model_attribute(self):
        node = self.__add_node(self.root, {'anki:model': 'Basic'})
        fp_node = Node(self.root, node)

        self.assertEqual('Basic', fp_node.get_model())

    def test_it_should_extract_the_id_from_the_node(self):
        node = self.__add_node(self.root, {'anki:model': 'Basic'})
        fp_node = Node(self.root, node)

        self.assertEqual('ID_1', fp_node.get_node_id())

    def test_it_should_extract_fields_from_the_anki_field_wildcard_attribute(self):
        node = self.__add_node(self.root, {'anki:field:Bar': 'Baz'})
        fp_node = Node(self.root, node)

        fields = fp_node.get_fields()
        self.assertTrue('Bar' in fields,
                        "Expected field list to contain a 'Bar' key")
        self.assertEqual('Baz', fields['Bar'])

    def test_it_should_replace_the_wildcard_character_with_the_node_text(self):
        node = self.__add_node(
            self.root, {'anki:field:Foo': 'Bar * Baz'}, 'Foo')
        fp_node = Node(self.root, node)

        fields = fp_node.get_fields()
        self.assertTrue('Foo' in fields,
                        "Expected field list to contain a 'Foo' key")
        self.assertEqual('Bar Foo Baz', fields['Foo'])

    def test_it_should_extract_the_node_text(self):
        text = 'This is the node text'
        node = self.__add_node(self.root, {'anki:field': 'Name'}, text)
        fp_node = Node(self.root, node)
        self.assertEqual(text, fp_node.get_text())

    def test_it_should_extract_fields_from_child_nodes(self):
        parent = self.__add_node(self.root, {
                                 'anki:field:Front': 'This is the front'})
        self.__add_node(parent, {
            'anki:field:Back': 'This is the back'})
        fp_node = Node(self.root, parent)
        fields = fp_node.get_fields()

        self.assertEqual('This is the back', fields['Back'])

    def test_it_should_extract_fields_from_nested_child_nodes(self):
        parent = self.__add_node(self.root, {
                                 'anki:field:Front': 'This is the front'})

        middle = self.__add_node(parent)
        self.__add_node(middle, {'anki:field:Back': 'This is the back'})

        fp_node = Node(self.root, parent)
        fields = fp_node.get_fields()

        self.assertEqual('This is the back', fields['Back'])

    def test_it_should_not_extract_fields_from_sub_notes(self):
        parent = self.__add_node(self.root)
        sub_note = self.__add_node(parent, {'anki:model': 'Basic'})
        self.__add_node(
            sub_note, {'anki:field:SubNote': 'This should be ignored'})

        fp_node = Node(self.root, parent)
        fields = fp_node.get_fields()

        self.assertFalse('SubNote' in fields)
