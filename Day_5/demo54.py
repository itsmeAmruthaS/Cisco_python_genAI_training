


from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} completed")
    return f"Task {name} result"

with ThreadPoolExecutor(max_workers=3) as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)
    f3 = executor.submit(task, 3)

    print(f1.result())
    print(f2.result())
    print(f3.result())

print("All tasks completed")


  