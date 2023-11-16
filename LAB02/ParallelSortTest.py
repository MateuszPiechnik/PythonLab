import multiprocessing
import random
import time
import matplotlib.pyplot as plt


def merge_sort(array):
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


def parallel_merge_sort(array, pool):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = pool.apply_async(merge_sort, args=(left,))
    right = pool.apply_async(merge_sort, args=(right,))
    left = left.get()
    right = right.get()

    return merge(left, right)


def test_parallel_merge_sort(processes, sizes):
    times = []
    for size in sizes:
        arr = [random.randint(0, 100) for _ in range(size)]
        pool = multiprocessing.Pool(processes)
        start = time.time()
        parallel_merge_sort(arr, pool)
        end = time.time()
        times.append(end - start)
    return times


if __name__ == "__main__":
    processes = [1, 5, 10, 20]
    sizes = [100, 1000, 100000, 1000000, 10000000]

    for process in processes:
        times = test_parallel_merge_sort(process, sizes)
        plt.plot(sizes, times, label=f'{process} processes')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Size of data')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()
