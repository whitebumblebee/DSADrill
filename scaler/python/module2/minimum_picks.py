class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        odd_min = 10000000000000000000001
        even_max = -10000000000000000000000
        for i in A:
            if i%2 != 0 and i < odd_min:
                odd_min = i
            elif i%2 == 0 and i > even_max:
                even_max = i
        return even_max - odd_min

