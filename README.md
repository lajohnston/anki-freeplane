# Anki Freeplane Importer Plugin

This is a plugin for the Anki flashcard system that allows you to convert Freeplane/Freemind .mm mindmaps into cards.

The plugin is currently a work in progress. The backend is working with unit tests, but does not yet have a user interface.

## Installation and example

This is just a proof-of-concept so far and only imports the mindmap found in the example directory. You can change this to point to a mindmap of your choice by editing the [mindmap.py](mindmap.py) file.

1. Copy this repository into the add-on directory (in Anki, click Tools > Add-ons > View files)
2. Restart Anki. You should now see 'Import mindmap' in the tools menu

If you are importing the example mindmap you might see an error notifying you that `FreeplaneModel` doesn't exist. You need to create this model in Anki with the fields specified in the mindmap attributes ('Front', 'Back').

If imported successfully you should see that a `FreeplaneDeck` deck has been created for you. This is specified in the mindmap in the node with the 'anki:deck' attribute. Inside this deck you will see that 2 cards have been created.

If you import again you'll notice that duplicate cards get created. To prevent this happening, edit the `FreeplaneModel` model to include a field named 'ID' and place it at the top. Delete the existing notes then import again. You'll notice that the ID gets populated with the Freeplane ID for that node, and subsequent imports won't import those cards again. If you edit the text for those nodes in Freeplane and re-import, the existing cards will be updated with the new text so long as the ID hasn't changed.

## Usage

## Attributes

Add the following attributes to the relevant mindmap nodes (using Alt + F9) to ensure they get imported correctly. An example mindmap can be found in the /examples directory.

### anki:deck

The name of the deck where descendant nodes will be imported into.

### anki:model

Identifies that the node can be converted to an Anki note. The value indicates what model its data should be imported into.

In Anki, if you create an 'ID' field as the first field in the model the plugin will automatically insert the node id into this and will use this when syncing future imports. Changing the text of the node in Freeplane and reimporting into Anki will therefore update the existing note rather than creating a whole new one.

### anki:field

Identifies the field the text node will be imported into.

### anki:field:\*

Example: 'anki:field:Back'

Defines a field value within the attributes. The attribute value will be used as the content. If the content contains an '\*' character this will be replaced by the text of the mindmap node.

### anki:modify (optional)

This optional attribute modifies or replaces the text of the field before importing it. Mindmap nodes often have abbreviated text that might not give enough information for a flashcard, so this attribute can be used to replace the text with something else when it gets imported. If the modified value contains an asterisk (\*) character, then the original text will be inserted at this point.

## Development

Run unit tests with `python -m unittest`.

The next step for this plugin will be creating a GUI so you can select the mindmap(s) you wish to import.
