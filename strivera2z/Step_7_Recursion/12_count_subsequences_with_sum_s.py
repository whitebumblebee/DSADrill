def count_subsequences_with_sum_s(ind, arr, n, k, sumi):
    if ind == n:
        if sumi == k:
            return 1
        return 0
    sumi += arr[ind]
    l = count_subsequences_with_sum_s(ind + 1, arr, n, k, sumi)
    sumi -= arr[ind]
    r = count_subsequences_with_sum_s(ind + 1, arr, n, k, sumi)
    return l + r


def main():
    arr = [1,2,3]
    n = len(arr)
    k = 3
    count = count_subsequences_with_sum_s(0, arr, n, k, 0)
    print(count)

if __name__ == '__main__':
    main()