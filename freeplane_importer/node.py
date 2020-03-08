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
            current = self.doc.find(
                './/node[@ID="' + current.get('ID') + '"]/..')

            if current is None or current.tag != 'node':
                return None

    ##
    # Returns a dict of field : value pairs for the given mindmap node
    ##
    def get_fields(self, fields={}):
        if self.fields is False:
            fields = self.__parse_fields(fields)

            for child in self.get_children():
                fields = child.get_fields(fields)

            self.fields = fields

        return self.fields

    ##
    # Extracts fields defined in 'anki:field:*' attributes and adds them to the
    # dict. If the attribute value contains '*' characters then these will be
    # replaced with the node text
    ##
    def __parse_fields(self, fields):
        attributes = self.element.findall('./attribute')
        if (not attributes):
            return fields

        node_text = self.element.get('TEXT')

        for attribute in attributes:
            name = attribute.get('NAME')
            if (name.startswith('anki:field:')):
                field = name[11:]
                value = attribute.get('VALUE')
                fields[field] = value.replace('*', node_text)

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
