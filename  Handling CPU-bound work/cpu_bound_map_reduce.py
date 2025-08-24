from concurrent.futures import ProcessPoolExecutor
from math import factorial
import time
start = time.perf_counter()
import sys
sys.set_int_max_str_digits(10000000)

# --- MAP function (CPU-bound) ---
def compute_factorial(n):
    return factorial(n)

# --- REDUCE function ---
def reduce_sum(values):
    return sum(values)

if __name__ == "__main__":
    numbers = [50000, 60000, 70000, 80000]

    with ProcessPoolExecutor() as pool:
        # MAP (distribute across processes)
        results = list(pool.map(compute_factorial, numbers))

        # REDUCE (sum factorials)
        total = reduce_sum(results)

    print("Factorials computed:", [str(r)[:20] + "..." for r in results])
    print("Sum of factorials:", str(total)[:20] + "...")

   
    end = time.perf_counter()
    print(f"Program finished in {end - start:.2f} seconds")