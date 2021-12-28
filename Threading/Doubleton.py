"""
Implement a doubleton pattern.(Even call should return first object, odd call should return second object)
"""

import threading
import time

class Doubleton:
    _instance1 = None
    _instance2 = None
    _call = 0
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # with cls._lock:
        cls._call += 1
        if cls._call % 2 == 0:
            if not cls._instance1:
              with cls._lock:
                if not cls._instance1:
                  cls._instance1 = super(Doubleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance1
        else:
            if not cls._instance2:
              with cls._lock:
                if not cls._instance2:
                  cls._instance2 = super(Doubleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance2

class Check(Doubleton):
    pass

if __name__ == '__main__':
    A, B, C, D = Check(), Check(), Check(), Check()
    print(A, B, C, D)