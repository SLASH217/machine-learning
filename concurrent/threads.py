import concurrent.futures
import time


# Simulating a network request that takes 1 second to respond
def fetch_data(url):
    print(f"Fetching {url}...")
    time.sleep(1)
    return f"Data from {url}"


if __name__ == "__main__":
    urls = [f"http://api.example.com/page_{i}" for i in range(1, 6)]
    start = time.time()

    # We use Threads here because we are WAITING on the network, not doing math
    # max_workers=5 means we fire off 5 requests simultaneously
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # executor.map handles the chunking and distribution automatically
        results = list(executor.map(fetch_data, urls))

    print(f"Results: {results}")
    # This will finish in ~1 second total, instead of 5 seconds!
    print(f"Finished in {time.time() - start:.2f} seconds")
