from constants import TONICS_INT


class Note:
    def __init__(self,
                 value: int,
                 duration: float = 0.,
                 time: float = 0.,
                 velocity: int = 75,
                 track: str = '0',
                 channel: int = 0,
                 annotation: object = None) -> None:
        self.track = track
        self.channel = channel
        self.value = value
        self.time = time
        self.duration = duration
        self.velocity = velocity
        self.annotation = annotation

    def __call__(self, *args, **kwargs):
        """
        Call this method anytime you want to output the arguments

        :param args:
        :param kwargs:
        :return: tuple of the arguments required for the addNote() method
        """
        return self.track, self.channel, self.value, self.time, self.duration, self.velocity, self.annotation

    def __str__(self):
        return self.getNoteValue()

    def getNoteValue(self):
        return TONICS_INT[self.value % 12] + str(self.value // 12 - 2)


if __name__ == '__main__':
    note = Note(60)
    print(note)
