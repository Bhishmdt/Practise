"""
Simulate deadlock.
"""

import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()

def A():
    lock1.acquire()
    time.sleep(1)
    lock2.acquire()

    print("A's Critical Section")

    lock1.release()
    lock2.release()

def B():
    lock2.acquire()
    time.sleep(1)
    lock1.acquire()

    print("B's Critical Section")

    lock2.release()
    lock1.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=A)
    t2 = threading.Thread(target=B)

    t1.start()
    t2.start()

    t1.join()
    t2.join()