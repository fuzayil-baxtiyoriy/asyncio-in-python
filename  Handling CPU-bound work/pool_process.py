from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool
import time

def say_hello(name: str) -> str:
    return f'Hi there, {name}'

def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Finished counting to {count_to} in {end - start}')
    return counter

if __name__ == "__main__":
    # with Pool() as process_pool:
    #     hi_jeff = process_pool.apply_async(say_hello, args=('Jeff',))
    #     hi_john = process_pool.apply_async(say_hello, args=('John',))
    #     print(hi_jeff.get())
    #     print(hi_john.get())
    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 3, 5, 22, 100000000]
        for result in process_pool.map(count, numbers):
            print(result)