from midiutil import MIDIFile as Midi
from midigen.midi.note import Note


class MIDIFile:
    def __init__(self, name='test'):
        self.name = name
        self.file = Midi()

    def addNote(self, note):
        """


        :type note: Note
        """
        self.file.addNote(*note())

    def addNotes(self, notes):
        """

        :type notes: list
        """
        for note in notes:
            self.addNote(note)
