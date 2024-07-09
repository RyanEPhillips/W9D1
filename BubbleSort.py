array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 1, 4, 2, 8]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(f"Sorted array: {bubble_sort(array1)}")
print(f"Sorted array: {bubble_sort(array2)}") 
