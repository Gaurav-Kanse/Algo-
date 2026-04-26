import time
import random

def mergeSort(arr):
    if len(arr) <=1:
        return arr
    mid  = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def prac():
    for n in [10, 100, 1000, 5000, 10000]:
        arr = [random.randint(1, 1000) for _ in range (n)]
        
        preview_input = arr[:10]
        
        start = time.time()
        sorted_arr = mergeSort(arr)
        end = time.time()
        
        preview_sorted  = sorted_arr[:10]
        print(f"{n:>8} | {str(preview_input):>35} | {str(preview_sorted):>35} | {(end - start):>12.6f}")
        
prac()