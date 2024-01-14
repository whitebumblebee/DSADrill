def recursive_insertion_sort(arr,i):
    if i == len(arr):
        return arr
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    return recursive_insertion_sort(arr, i+1)

def main():
    arr = [4,3,2,1]
    print(recursive_insertion_sort(arr, 0))

if __name__ == '__main__':
    main()