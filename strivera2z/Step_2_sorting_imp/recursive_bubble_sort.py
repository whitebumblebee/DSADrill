def bubble_sort_recursive(arr, i):
    if i < 0:
        print(arr)
        return
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    bubble_sort_recursive(arr, i-1)

def main():
    arr = [5,4,3,2,1]
    bubble_sort_recursive(arr, len(arr)-1)

if __name__ == '__main__':
    main()
