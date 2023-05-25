"""
We will solve problems related to print n to 1 using recursion

"""

"""
Question: Print N to 1 using recursion.
link: https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
"""

# My solution

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)