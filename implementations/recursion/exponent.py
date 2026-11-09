"""
Write code recursively to find the exponential function m ^ n
"""

def exponent_recursive(m, n):
    if n == 1:
        return m
    return m * exponent_recursive(m, n-1)

if __name__ == "__main__":
    print("Give the value of m and n to calculate m ^ n")
    m, n = list(map(int, input().split()))
    result = exponent_recursive(m, n)
    print("With Recursion")
    print(result)
    print("Without Recursion")
    print(m ** n)


