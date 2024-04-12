import os
import time  # type: ignore
from multiprocessing import Process, cpu_count

def process():
    print(f'The process id: {os.getpid()}')
    for _ in range(1000000):
        pass 

# Multi-processing
if __name__ == '__main__':
    start = time.perf_counter()
    processes = [Process(target=process) for _ in range(cpu_count())]
    
    # Start all processes
    for p in processes:
        p.start()

    # Join all processes (wait for them to finish)
    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f'All processes completed in {round(end-start, 2)} seconds')
