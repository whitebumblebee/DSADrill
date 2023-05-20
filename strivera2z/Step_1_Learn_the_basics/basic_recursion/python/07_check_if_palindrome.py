"""
We will solve problems related to print n to 1 using recursion

"""

"""
Question: check if string is palindrome using recursion
link: https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
"""

#User function Template for python3
import sys
class Solution:
    def get_reverse_string_recursive(self, s, s1, n):
        if n < 0:
            return s1
        s1 += s[n]
        return self.get_reverse_string_recursive(s, s1, n-1)
    def isPalindrome(self, S):
        # code here
        n = len(S) - 1
#         sys.setrecursionlimit(n*10)
        s1 = ''
        reversed_string = self.get_reverse_string_recursive(S, s1, n)
        if S == reversed_string:
            return 1
        else:
            return 0
        
"""
check palindrome logic by striver
"""

import sys
class Solution:
    # @param A : string
    # @return an integer
    def solve_recurse(self, s, i, n):
        if i <= n//2:
            if s[i] == s[n-i-1]:
                i += 1
                return self.solve_recurse(s, i, n)
            else:
                return 0
        return 1
    def solve(self, A):
        n = len(A)
        sys.setrecursionlimit(n*10)
        return self.solve_recurse(A, 0, n)