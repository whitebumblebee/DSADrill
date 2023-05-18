"""
We will solve problems related to print n to 1 using recursion

"""

"""
Question: Print N to 1 using recursion.
link: https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
"""

# My solution
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