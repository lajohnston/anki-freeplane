# Anki Freeplane Importer Plugin

## 
This is a plugin for the Anki flashcard system that allows you to import cards from annotated Freeplane/Freemind mindmaps.

The plugin is currently a work in progress. The backend is working with unit tests, but does not yet have a user interface.

If you create an 'ID' field as the first field in the model, the plugin will automatically insert the node id into this and will use this when syncing future imports. Changing the text of the node in Freeplane and reimporting into Anki will therefore update the existing note rather than creating a whole new one.

## Attributes
The nodes in the mindmap should be annotated with the following named attributes, which can be accessed in Freeplane using Alt + F9. An example mindmap can be found in the examples directory.

###anki:deck
The name of the deck to import all ancestor nodes into. When this is used on a node, all ancestor nodes (including nested children) will inherit this deck.

###anki:model
Identifies that the node is an Anki note, and what model its fields should be imported into.

###anki:field
Identifies a field within the model that the text node will be imported into.

###anki:modify
This optional attributes modifies or replaces the text of field before importing it. Mindmap nodes often have abbreviated text that might not give enough information for a flashcard, so this attribute can be used to add additional text. If the modify value contains an asterisk (*) character, then the original text will be inserted at this point. 