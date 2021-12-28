"""
Print series 010203040506. Using multi-threading 1st thread will print only 0 2nd thread will print only even numbers and 3rd thread print only odd numbers.
"""
import threading
lockZero = threading.Lock()
lockOdd = threading.Lock()
lockEven = threading.Lock()

def print_zero(n):
    global x

    for _ in range(n):
        lockZero.acquire()
        x += 1
        print(0)
        if x % 2:
            lockOdd.release()
        else:
            lockEven.release()

def print_even(n):
    global x

    for _ in range(n):
        lockEven.acquire()
        print(x)
        lockZero.release()

def print_odd(n):
    global x

    for _ in range(n):
        lockOdd.acquire()
        print(x)
        lockZero.release()

if __name__ == '__main__':
    x = 0
    n = 3
    lockOdd.acquire()
    lockEven.acquire()
    t1 = threading.Thread(target=print_zero, args=(n * 2,))
    t2 = threading.Thread(target=print_odd, args=(n,))
    t3 = threading.Thread(target=print_even, args=(n,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
