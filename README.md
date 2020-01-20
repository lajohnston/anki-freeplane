# Anki Freeplane Importer Plugin

This is a plugin for the Anki flashcard system that allows you to convert Freeplane/Freemind .mm mindmaps into cards.

The plugin is currently a work in progress. The backend is working with unit tests, but does not yet have a user interface.

## Attributes

Add the following attributes to the relevant mindmap nodes (using Alt + F9) to ensure they get imported correctly. An example mindmap can be found in the /examples directory.

### anki:deck

The name of the deck where ancestor nodes will be imported into.

### anki:model

Identifies that the node can be converted to an Anki note. The value indicates what model its data should be imported into.

In Anki, if you create an 'ID' field as the first field in the model the plugin will automatically insert the node id into this and will use this when syncing future imports. Changing the text of the node in Freeplane and reimporting into Anki will therefore update the existing note rather than creating a whole new one.

### anki:field

Identifies a field within the model that the text node will be imported into.

### anki:modify

This optional attributes modifies or replaces the text of field before importing it. Mindmap nodes often have abbreviated text that might not give enough information for a flashcard, so this attribute can be used to add additional text. If the modify value contains an asterisk (\*) character, then the original text will be inserted at this point.
