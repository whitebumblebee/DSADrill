
def is_palindrome(number):
    temp = number 
    reverse_number = 0

    while temp != 0:
        rd = temp % 10
        reverse_number = reverse_number * 10 + rd
        temp = temp // 10

    return number == reverse_number

if __name__ == "__main__":
    num = int(input())
    print(is_palindrome(num))