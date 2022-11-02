class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def reverse_array(self, arr, si, ei):
        while si <= ei:
            arr[si], arr[ei] = arr[ei], arr[si]
            si+=1
            ei-=1
        return arr
    def rotate_left(self, arr, k):
        N = len(arr)
        if k > N:
            k = k % N
        arr = self.reverse_array(arr, 0, k-1)
        arr = self.reverse_array(arr, k, N-1)
        arr = self.reverse_array(arr, 0, N-1)
        return arr

    def solve(self, A, B):
        result = []
        for i in B:
            result.append(self.rotate_left(A, i))
        return result
