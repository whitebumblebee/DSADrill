"""
given an integer find the the number of digits of that number
"""

def count_digit(number):
    ans = 0
    while number != 0:
        number = number // 10
        ans += 1

    return ans

if __name__ == "__main__":
    print(count_digit(9253))