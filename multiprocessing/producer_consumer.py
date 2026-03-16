import multiprocessing
import time

def producer(queue):
    print("Producer: Starting the assembly line...")
    for item in ["Image_1", "Image_2", "Image_3"]:
        time.sleep(0.5) # Simulate the time it takes to download
        print(f"Producer: Downloaded {item}, putting it on the belt.")
        queue.put(item) # Drop data into the shared pipe

    # Send a "Poison Pill" to tell the consumer we are done
    queue.put("DONE")

def consumer(queue):
    print("Consumer: Waiting for items...")
    while True:
        # Grab data from the pipe
        item = queue.get()

        # Check for the Poison Pill
        if item == "DONE":
            print("Consumer: Belt is empty. Going home.")
            break

        print(f"Consumer: Received {item}. Resizing now...")
        time.sleep(1) # Simulate the heavy math of image processing

if __name__ == '__main__':
    # Create the shared conveyor belt
    belt = multiprocessing.Queue()

    # Assign the jobs to two separate processes
    p1 = multiprocessing.Process(target=producer, args=(belt,))
    p2 = multiprocessing.Process(target=consumer, args=(belt,))

    # Start both at exactly the same time
    p1.start()
    p2.start()

    p1.join() # this tells the main process to wait for the p1 and p2 processes to finish before terminating
    p2.join() # otherwise it would cause orphan processes.

# Solving the producer consumer problem using multiprocessing in python

# Producer -> creates item -> puts in shared pipeline

# Consumer -> consumes item -> removes from shared pipeline

# The actual effect: Producer runs independently in Process 1,
#  Consumer in Process 2,
#  they coordinate through OS pipes managed by the Queue's central broker.

# Main Process Timeline:
# ├─ p1.start() → p1 begins running (doesn't wait, returns immediately)
# ├─ p2.start() → p2 begins running (doesn't wait, returns immediately)
# ├─ p1.join() → BLOCKS HERE until p1 finishes
# │  (p1 and p2 run in parallel while main is blocked)
# ├─ p2.join() → BLOCKS HERE until p2 finishes
# └─ Program ends

# P1 (Producer) Timeline:
# ├─ Create items, put in queue
# └─ Finish, process exits → wakes main from p1.join()

# P2 (Consumer) Timeline:
# ├─ Get items from queue, process
# └─ Receive "DONE", break loop, process exits → wakes main from p2.join()