"""
We will solve problems related to reversing an array

"""

"""
Question: Print N to 1 using recursion.
link: https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
"""

# My solution

def reverse_array_recursion(arr, i, j):
    if i > j:
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    return reverse_array_recursion(arr, i+1, j-1)

print(reverse_array_recursion([1,2,3,4,5], 0, 4))


"""
Reverse a string similarly
"""

import sys
def get_reverse_string_recursive(s, s1, n):
    if n < 0:
        return s1
    s1 += s[n]
    return get_reverse_string_recursive(s, s1, n-1)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s = input()
    n = len(s)
    sys.setrecursionlimit(n*10)
    s1 = ''
    print(get_reverse_string_recursive(s, s1, n-1))
    return 0

if __name__ == '__main__':
    main()

"""
Solutions by striver if different from mine
"""

"""
For reversing array with single pointer, we can use i as the first pointer and n-i-1 as the second pointer.
So, code would look something like below
"""
    
def reverse_array_recursion(arr, i):
    n = len(arr)
    if i >= n//2:
        return arr
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return reverse_array_recursion(arr, i+1)

print(reverse_array_recursion([1,2,3,4,5], 0))