"""
Using Recursion to find sum of first n natural numbers
"""
def sum_recursively(num):
    if num == 1:
        return 1
    return num + sum_recursively(num - 1)

if __name__ == "__main__":
    num = int(input("Give the value of n:"))
    result = sum_recursively(num)
    print("With Recursion")
    print(result)
    print("Using the formula")
    print(num * (num + 1) // 2)