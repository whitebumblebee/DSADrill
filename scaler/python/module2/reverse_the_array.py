class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        arr = list(A)
        i = len(arr) - 1
        j = 0
        while j <= i:
            arr[i],arr[j] = arr[j], arr[i]
            i-=1
            j+=1
        return arr