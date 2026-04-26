import time 
import random 

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    left = [x for x in arr if x < pivot]
    return quickSort(left)+mid+quickSort(right)

def startf():
    for n in [10,100,1000,5000,10000]:
        arr = [random.randint(1,10000) for _ in range(n)]
        preview_input = arr[:10]
        
        start = time.time()
        sorted_arr = quickSort(arr)
        end = time.time()
        
        preview_sorted = sorted_arr[:10]
        print(f"{n:>8} | {str(preview_input):>10} | {str(preview_sorted):>10} | {(end - start):>12.6f}")
        
startf()