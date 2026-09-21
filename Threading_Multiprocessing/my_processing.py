import threading
import multiprocessing
import time

def cpu_bound_task(n):
    total = 0
    for i in range(n):
        total += i**2 *0.5
    return total

def multi_threading(n,num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target = cpu_bound_task, args = (n,))
        threads.append(thread)
        thread.start()
    for j in threads:
        j.join()

def multi_processing(n,num_processes):
    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target = cpu_bound_task, args = (n,))
        processes.append(process)
        process.start()
        print("hello")
    for j in processes:
        j.join()
if __name__ == "__main__":
    start_time = time.time()
    multi_threading(65**4,4)
    print(f"Total time = {time.time()-start_time}")

    start_time = time.time()
    multi_processing(65**4,4)
    print(f"Total time = {time.time()-start_time}")