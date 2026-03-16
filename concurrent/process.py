import concurrent.futures
import time
import random


# Simulating a heavy CPU task where some files take longer than others
def process_heavy_file(filename):
    processing_time = random.uniform(0.5, 2.0)
    time.sleep(processing_time)
    return f"{filename} (Took {processing_time:.2f}s)"


if __name__ == "__main__":
    files = [f"Image_{i}.png" for i in range(1, 6)]
    print(files)
    start = time.time()

    # We use Processes here because we are pretending this is heavy CPU math
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 1. We "submit" the tasks to the workers. This returns a dictionary of "Future" objects.
        # A Future is basically a tracking ticket for a task that isn't done yet.
        future_to_file = {
            executor.submit(process_heavy_file, file): file for file in files
        }

        # 2. as_completed() watches those tracking tickets.
        # The moment ANY worker finishes its math, it spits the result out here.
        for future in concurrent.futures.as_completed(future_to_file):
            # We can print or update a progress bar in real-time!
            result = future.result()
            print(f"UI UPDATE: Successfully processed -> {result}")

    print(f"All files processed in {time.time() - start:.2f} seconds")
