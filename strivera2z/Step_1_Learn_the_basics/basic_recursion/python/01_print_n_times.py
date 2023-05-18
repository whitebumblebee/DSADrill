"""
We will solve problems related to print something n times using recursion

"""

"""
Question 1: Print 1 to N without Loop
https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-1-to-n-without-using-loops
"""

# My solution
class Solution:    
    #Complete this function
    num = 1
    def printNos(self,N):
        #Your code here
        if self.num > N:
            return
        print(self.num, end=" ")
        self.num += 1
        self.printNos(N)

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()


"""
Question 2: Print Name n times using Recursion
Problem link: https://practice.geeksforgeeks.org/problems/print-gfg-n-times/1
"""

class Solution:
    num = 1
    def printGfg(self, n):
        # Code here
        if self.num > n:
            return
        print("GFG", end=" ")
        self.num+=1
        self.printGfg(n)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()



