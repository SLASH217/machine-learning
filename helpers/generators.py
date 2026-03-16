import sys

# THE FATAL WAY (List Comprehension)
# This asks the OS for roughly 8 Gigabytes of RAM instantly.
# Your computer will likely freeze or crash.
# massive_list = [x * x for x in range(1_000_000_000)]
# print(sum(massive_list))

# THE CRITICAL WAY (Generator Expression)
# Notice the () instead of [].
# massive_generator = (x * x for x in range(1_000_000_000))

# # This uses practically 0 bytes of RAM.
# print(f"Memory used: {sys.getsizeof(massive_generator)} bytes")

# # sum() pulls one number, adds it to the total, and immediately deletes it from RAM.
# total = sum(massive_generator)
# print(total)



# THE CRITICAL WAY (Custom Yield Function)
def extract_errors_from_massive_file(filepath):
    # open() creates a pointer to the file on your hard drive,
    # but does NOT load the text into RAM yet.
    with open(filepath, "r") as file:
        for line in file:
            # We check one single line at a time
            if "ERROR 404" in line:
                # We pause the function and hand this single line back to the main code
                yield line.strip()

# Usage:
# The generator pipeline is perfectly memory-safe.
# It reads 50GB of text, but only 1 line ever exists in RAM at any given microsecond.
error_generator = extract_errors_from_massive_file("massive_50GB_server_logs.csv")

# We can safely write the filtered results to a new, smaller file
with open("clean_training_data.csv", "w") as clean_file:
    for error_line in error_generator:
        clean_file.write(error_line + "\n")

print("Finished filtering 50GB without crashing!")