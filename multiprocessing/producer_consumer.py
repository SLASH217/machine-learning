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

    p1.join()
    p2.join()