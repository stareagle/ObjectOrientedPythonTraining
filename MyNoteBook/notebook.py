import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """
    Represent a note in the Notebook.
    Match against a string in searches and store tags for each note.
    """
    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo an optional space seperated tags.
        Automatically set the note's creation date and a unique id
        :param memo:
        :param tags:
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Determine if this note matches the filter text.
        Return True if it matches, False otherwise.
        :param filter:
        :return: Boolean
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    Represent a collection of notes that can be tagged, modified and searched.
    """
    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list
        :param memo:
        :param tags:
        :return:
        """
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its memo to the given value.
        :param note_id:
        :param memo:
        :return:
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its tags to the given value.
        :param note_id:
        :param tags:
        :return:
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        else:
            return False

    def search(self, filter):
        """
        Find all notes that match the given filter string.
        :param filter:
        :return: list
        """
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        """
        Locate the note with the given id
        :param note_id:
        :return:
        """
        for note in self.notes:
            if note.id == str(note_id):
                return note
            return None


