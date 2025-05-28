import numpy as np
import time
import matplotlib.pyplot as plt

def systolic_bubble_sort(arr):
    n = len(arr)
    pe = arr.copy()  # Each PE starts with one element

    for t in range(n - 1):  # Bubble sort requires n-1 passes
        for i in range(n - 1 - t):
            if pe[i] > pe[i + 1]:
                pe[i], pe[i + 1] = pe[i + 1], pe[i]
    return pe

# Test and benchmark
def benchmark_sorting():
    sizes = [10, 100, 1000, 5000, 10000]
    times = []

    for size in sizes:
        data = np.random.randint(0, 10000, size)
        start = time.time()
        sorted_data = systolic_bubble_sort(data)
        end = time.time()
        times.append(end - start)
        print(f"Sorted {size} elements in {end - start:.4f} seconds")

    # Plot results
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Systolic Array Bubble Sort Performance")
    plt.grid(True)
    plt.show()

benchmark_sorting()
