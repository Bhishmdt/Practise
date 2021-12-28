"""
Implement thread safe timer with start, stop and reset functionality.
"""

from threading import Thread, Lock, Condition

class Timer:
    _state = 0
    _cv = Condition(Lock())

    def __init__(self, setTime = 0):
        self.setTime = setTime

    def reset(self):
        self.currentTime = self.setTime
        self._state = 0

    def stop(self):
        self._state = -1

    def start(self):
        self._state = 0

    def run(self):
