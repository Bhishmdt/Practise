import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 sec..')
    time.sleep(1)
    print('Done Sleeping..')

# do_something()
# do_something()

"""
Sleeping for 1 sec..
Done Sleeping..
Sleeping for 1 sec..
Done Sleeping..
Finished in 2.0 seconds.
"""

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()

"""
Sleeping for 1 sec..
Sleeping for 1 sec..Finished in 0.0 seconds.

Done Sleeping..Done Sleeping..
"""

# t1.join()
# t2.join()

"""
Sleeping for 1 sec..Sleeping for 1 sec..

Done Sleeping..Done Sleeping..

Finished in 1.0 seconds.
"""
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

"""
Sleeping for 1 sec..
Sleeping for 1 sec..
Sleeping for 1 sec..
Sleeping for 1 sec..
Sleeping for 1 sec..
Sleeping for 1 sec..Sleeping for 1 sec..
Sleeping for 1 sec..
Sleeping for 1 sec..Sleeping for 1 sec..
Done Sleeping..
Done Sleeping..
Done Sleeping..
Done Sleeping..Done Sleeping..
Done Sleeping..Done Sleeping..
Done Sleeping..Done Sleeping..
Done Sleeping..
Finished in 1.0 seconds.
"""

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds.')

if __name__ == '__main__':
    pass
