"""
Question: Sum of first n numbers
link: https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=sum-of-first-n-terms
"""

# My solution

class Solution:
    def sumOfSeries(self,N):
        #code here
        if N == 0:
            return 0
        sum = N ** 3 + self.sumOfSeries(N-1)
        return sum
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends


