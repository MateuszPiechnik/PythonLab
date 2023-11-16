import random

randomList = []

def randomNumbers(N):
    for i in range(0,N):
        randomList.append(random.randint(-5, 20))

def bubbleSort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers

def selectSort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp
    return numbers

randomNumbers(10)
print ("Not sorted:", randomList)

print("Sorted with bubbleSort:", bubbleSort(randomList))
print("Sorted with selectSort:", selectSort(randomList))
print("Sorted with sorted():", sorted(randomList))


