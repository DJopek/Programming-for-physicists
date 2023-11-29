import numpy as np
import time
import random

n = int(input("input number of numbers: "))

# random_array =  np.random.rand(n).tolist()
random_array = np.random.rand(n)

print(random_array)

def bubble_sort(n):
    for i in range (0,n):
        for j in range (0,n-i-1):
            if random_array[j+1] < random_array[j] :
                x = random_array[j]
                y = random_array[j+1]
                random_array[j+1] = x
                random_array[j] = y

    print(random_array)

def selection_sort(n):

    for i in range (0,n):
        min = i
        for j in range(i+1,n):
            if random_array[j] < random_array[min]:
                min = j
        x = random_array[i]
        random_array[i] = random_array[min]
        random_array[min] = x

    print(random_array)

def quick_sort(arr):

    # print(arr)
    # print(len(arr))

    if len(arr) <= 1:
        return arr
    
    else:

        pivot = arr[0]
        right = []
        left = []

        for item in arr:

            if item < pivot :
                left.append(item)
            elif pivot < item :
                right.append(item)
        
    return quick_sort(left) + [pivot] + quick_sort(right)
                    


def measure_time(sort, array):
    start_time = time.time()
    sort(random_array)
    end_time = time.time()
    result_time = end_time - start_time
    print(result_time)

# bubble_sort(n)
# selection_sort(n)
# print(quick_sort(random_array))
measure_time(quick_sort, random_array)