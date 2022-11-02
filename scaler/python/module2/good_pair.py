class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        for i in range(N):
            for j in range(i+1,N):
                if A[i]+A[j] == B:
                    return 1
        return 0