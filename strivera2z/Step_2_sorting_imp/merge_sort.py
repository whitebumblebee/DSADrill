def merge(arr, low, mid, high):
    temp_arr = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp_arr.append(arr[left])
            left += 1
        else:
            temp_arr.append(arr[right])
            right += 1
    while left <= mid:
        temp_arr.append(arr[left])
        left += 1
    while right <= high:
        temp_arr.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp_arr[i-low]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def main():
    arr = [5,4,3,2,1]
    print("before sorting")
    print(arr)
    merge_sort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
