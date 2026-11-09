import math
def factorial_recursive(num):
    if num == 0:
        return 1
    return num * factorial_recursive(num - 1)

if __name__ == "__main__":
    n = int(input("Enter a number:"))
    result = factorial_recursive(n)
    print("With recursion")
    print(result)
    print("Without recursion")
    print(math.factorial(n))