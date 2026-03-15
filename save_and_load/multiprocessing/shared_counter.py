import multiprocessing

import time

def worker_task (shared_counter, lock):

  time.sleep(0.1)

  with lock:
    shared_counter.value +=1

if __name__ == '__main__':
  # i means integer. we start the counter at 0
  counter = multiprocessing.Value('i', 0)

  lock = multiprocessing.Lock()

  processes = []
  start = time.time()
  for _ in range(10):
    p = multiprocessing.Process(target=worker_task, args=(counter, lock))
    processes.append(p)
    p.start() # turn the worker on
  # tell the main script to wait until all 10 workers are finished.
  for p in processes:
    p.join()

  print(f"Final shared counter value: {counter.value} and time: {time.time() - start}")