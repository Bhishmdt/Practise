"""
Print series 010203040506. Using multi-threading 1st thread will print only 0 2nd thread will print only even numbers and 3rd thread print only odd numbers.
"""

from threading import Thread, Lock, Condition

def print_zero(n):
    global x
    global state
    for _ in range(n):
        with cv:
            while state not in (0, 2):
                cv.wait()
            state += 1
            x += 1
            print(0)
            cv.notify_all()

def print_even(n):
    global x
    global state
    for _ in range(n):
        with cv:
            while state != 3:
                cv.wait()
            print(x)
            state = 0
            cv.notify_all()

def print_odd(n):
    global x
    global state
    for _ in range(n):
        with cv:
            while state != 1:
                cv.wait()
            print(x)
            state = 2
            cv.notify_all()

if __name__ == '__main__':
    x = 0
    state = 0
    n = 3
    cv = Condition(Lock())
    t1 = Thread(target=print_zero, args=(n * 2, ))
    t2 = Thread(target=print_odd, args=(n, ))
    t3 = Thread(target=print_even, args=(n, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()