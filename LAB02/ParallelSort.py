import multiprocessing
import random
import time
import matplotlib.pyplot as plt


def merge_sort(array):
    if isinstance(array, int):
        return  array
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    merged_array += left[i:]
    merged_array += right[j:]

    return merged_array


def test_parallel_merge_sort(processes, sizes):
    times = []
    for size in sizes:
        arr = [random.randint(0, 100) for _ in range(size)]
        with multiprocessing.Pool(processes) as p:
            start = time.time()
            p.map(merge_sort, arr)
            end = time.time()
            times.append(end - start)
    return times


if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    sizes = [10**2, 10**3, 100**4, 10**6, 10**8]

    for process in processes:
        times = test_parallel_merge_sort(process, sizes)
        plt.plot(sizes, times, label=f'{process} processes')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Size of data')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()