"""
Program with start(), join(), acquire(), release(), sleep().
"""

import threading
import time
lock = threading.Lock()

def C():
    time.sleep(5)
    print("C's Critical Section")

def D():
    print("D's Critical Section")

def A():
    lock.acquire()
    time.sleep(5)
    print("Lock acquired by A")
    print("A's Critical Section")
    lock.release()
    print("Lock released by A")

def B():
    lock.acquire()
    print("Lock acquired by B")
    print("B's Critical Section")
    lock.release()
    print("Lock released by B")

if __name__ == '__main__':
    t1 = threading.Thread(target=C)
    t2 = threading.Thread(target=D)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    t1 = threading.Thread(target=A)
    t2 = threading.Thread(target=B)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    """
D's Critical Section
C's Critical Section
Lock acquired by A
A's Critical Section
Lock released by A
Lock acquired by B
B's Critical Section
Lock released by B
    """