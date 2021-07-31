from threading import Thread, Condition
import time

class Producer(Thread):
    def run(self):
        global CAPACITY, buffer

        global condition

        items_produced = 0
        counter = 0

        while items_produced < 20:
            condition.acquire()

            if len(buffer) == CAPACITY:
                print("Buffer full")
                condition.wait()
                print("Space in Queue")
            counter += 1
            buffer.append(counter)
            print("Producer produced :", counter)

            condition.notify()
            condition.release()

            time.sleep(1)

            items_produced += 1

class Consumer(Thread):
    def run(self):
        global CAPACITY, buffer

        global condition

        items_consumed = 0
        while items_consumed < 20:
            condition.acquire()
            if not buffer:
                print("Nothing in queue")
                condition.wait()
                print("Producer added item")
            item = buffer.pop(0)

            print("Consumer consumed item: ", item)

            condition.notify()
            condition.release()

            time.sleep(2.5)

            items_consumed += 1

if __name__ == '__main__':
    CAPACITY = 10
    buffer = []
    condition = Condition()

    producer = Producer()
    consumer = Consumer()

    consumer.start()
    producer.start()

    producer.join()
    consumer.join()
    """
    Nothing in queue
    Producer produced : 1
    Producer added item
    Consumer consumed item:  1
    Producer produced : 2
    Producer produced : 3
    Consumer consumed item:  2
    Producer produced : 4
    Producer produced : 5
    Consumer consumed item:  3
    Producer produced : 6
    Producer produced : 7
    Producer produced : 8
    Consumer consumed item:  4
    Producer produced : 9
    Producer produced : 10
    Consumer consumed item:  5
    Producer produced : 11
    Producer produced : 12
    Producer produced : 13
    Consumer consumed item:  6
    Producer produced : 14
    Producer produced : 15
    Consumer consumed item:  7
    Producer produced : 16
    Producer produced : 17
    Buffer full
    Consumer consumed item:  8
    Space in Queue
    Producer produced : 18
    Buffer full
    Consumer consumed item:  9
    Space in Queue
    Producer produced : 19
    Buffer full
    Consumer consumed item:  10
    Space in Queue
    Producer produced : 20
    Consumer consumed item:  11
    Consumer consumed item:  12
    Consumer consumed item:  13
    Consumer consumed item:  14
    Consumer consumed item:  15
    Consumer consumed item:  16
    Consumer consumed item:  17
    Consumer consumed item:  18
    Consumer consumed item:  19
    Consumer consumed item:  20
    """
