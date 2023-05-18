"""
We will solve problems related to print n to 1 using recursion

"""

"""
Question: Print N to 1 using recursion.
link: https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
"""

# My solution

class Solution:
    def printNos(self, n):
        # Code here
        if n == 0:
            return
        print(n, end=" ")
        n-=1
        self.printNos(n)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends