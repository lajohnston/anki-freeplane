from .node import Node
import copy


class Reader:
    ##
    # Returns an array of notes. Each note is a dict object with the
    # following keys:
    #
    # deck		the name of the deck the note belongs in
    # model		the model (note type) of the note
    # fields	field: value pairs of all fields in the note
    # id		the id of the node in the mindmap
    ##
    def get_notes(self, doc):
        self.note_nodes = doc.findall('.//attribute[@NAME="anki:model"]/..')

        notes = []
        for element in self.note_nodes:
            node = Node(doc, element)
            notes.append(copy.deepcopy(node.to_dict()))

        return notes
