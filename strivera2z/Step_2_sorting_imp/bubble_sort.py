def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5,44,3,2,1]))

# striver's implementation

def bubble_sort_s(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        did_swap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap = 1
        if did_swap == 0:
            break
    return arr

print(bubble_sort_s([5,44,3,2,1]))