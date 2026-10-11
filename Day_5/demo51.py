

import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

start = time.perf_counter()
task("Task 1")
task("Task 2")
end = time.perf_counter()


print(f"Total time taken: {end - start} seconds")
