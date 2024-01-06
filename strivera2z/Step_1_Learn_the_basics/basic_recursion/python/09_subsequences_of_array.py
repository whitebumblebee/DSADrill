# We need to find all the subsequences of array
# for this we are going to use recursion

def subsequences(index, arr, ds, n):
    if index == n:
        print(ds)
        return
    # case of not pick
    subsequences(index+1, arr, ds, n)
    ds.append(arr[index])
    # case of pick
    subsequences(index+1, arr, ds, n)
    ds.pop()
    # case of not pick could have been here too
    #  subsequences(index+1, arr, ds, n)
    
    

def main():
    arr = [3,1,2, 4]
    n = len(arr)
    ds = []
    subsequences(0, arr, ds, n)

main()
