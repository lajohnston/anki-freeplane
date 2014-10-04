from freeplane_importer import FreeplaneReader

reader = FreeplaneReader('../../../Dropbox/Anki deck mindmap.mm')
notes = reader.parse_notes()

