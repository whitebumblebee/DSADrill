def print_only_one_subsequence_with_sum_k(arr, ind, n, ds, sumi, k):
    if ind >= n:
        if sumi == k:
            print(ds)
            return True
        return False
    ds.append(arr[ind])
    sumi += arr[ind]
    if print_only_one_subsequence_with_sum_k(arr, ind+1, n, ds, sumi, k) == True:
        return True
    ds.pop()
    sumi -= arr[ind]
    if print_only_one_subsequence_with_sum_k(arr, ind+1, n, ds, sumi, k) == True:
        return True
    
    return False

def main():
    arr = [1,2,3]
    n = len(arr)
    k = 3
    ds = []
    print_only_one_subsequence_with_sum_k(arr, 0, n, ds, 0, k)

if __name__ == "__main__":
    main()