from note import Note


class Chord:
    def __init__(self, *args: Note, chord_type=""):
        self.notes = []
        for arg in args:
            self.notes.append(arg) if type(arg) == Note else None
        self.chord_type = chord_type