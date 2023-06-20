import math


class TimeSignature:
    def __init__(self, time, clocks_per_tick=24, notes_per_quarter=8):
        """
        :param time: time signature in the format "[NUMBER]/[NUMBER]"
        :type time: str
        """
        self._time = time
        self._numerator, self._denominator = int(time.split('/')[0]), math.log2(int(time.split('/')[1]))
        self._clocks_per_tick = clocks_per_tick
        self._notes_per_quarter = notes_per_quarter

    def __call__(self, *args, **kwargs):
        return self._time, self._numerator, self._denominator, self._clocks_per_tick, self._notes_per_quarter
