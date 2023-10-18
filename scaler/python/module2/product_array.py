class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        prod = 1
        for i in A:
            prod *= i
        new_A = []
        for i in A:
            new_A.append(prod//i)
        return new_A