# 1. The CPU Crusher: Finding Prime Numbers (Data Parallelism)
# The Problem: You have a massive list of large numbers, and you need to check if each one is a prime number.
# Doing this on a single core takes forever because the math is heavy.
# The Solution: Use multiprocessing.Pool to chop the list into chunks and hand a chunk to each CPU core.

import multiprocessing

import time

import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # numbers = [15485863, 15485867, 15485869, 15485873, 15485881] * 10
    numbers = [1548586399, 1548586799, 1548586999, 1548587399, 1548588199] * 5350
    start = time.time()

    # for i in numbers:
    #     is_prime(i)
    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)
    print(f"Checked {len(numbers)} numbers in {time.time() - start:.4f} seconds.")

# If we use multiprocessing for too easy problems it will increase the time instead of decreasing it due to:
# Process Creation Overhead and Inter-Process Communication (IPC)
# The Spin-up Tax: The OS has to carve out brand new, isolated blocks of RAM. It then has to boot up an entirely
# separate Python interpreter for every single core on your machine.
# The Pickling Tax: The main process has to take your list of numbers, serialize (pickle) them into bytes,
# and push them through an OS pipe to the isolated workers.
# The Unpickling Tax: The workers have to un-pickle the bytes back into Python integers.
# The Return Tax: Once the math is done, the workers have to pickle the True/False answers,
# send them back through the pipe, and the main process has to unpickle them and stitch the list back together.
