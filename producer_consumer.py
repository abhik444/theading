import threading
import queue
import time
import random

# Shared queue
queue_size = 5
shared_queue = queue.Queue(queue_size)

# Producer function
def producer():
    while True:
        item = random.randint(1, 100)  # Produce a random item
        try:
            shared_queue.put(item, block=False)  # Put the item in the queue
            print(f"Produced {item}")
        except queue.Full:
            print("Queue is full. Producer waiting...")
        time.sleep(random.random())  # Simulate variable production time

# Consumer function
def consumer():
    while True:
        try:
            item = shared_queue.get(block=False)  # Get an item from the queue
            print(f"Consumed {item}")
        except queue.Empty:
            print("Queue is empty. Consumer waiting...")
        time.sleep(random.random())  # Simulate variable consumption time

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish (should never happen in this example)
producer_thread.join()
consumer_thread.join()
