"""
given a list of numbers find the second largest element in the list
"""
# My approach
def get_second_largest_number(l):
    largest_element = max(l)
    second_largest_element = -123456789

    for num in l:
        if num >= second_largest_element and num < largest_element:
            second_largest_element = num

    return second_largest_element

# teacher's approach: NAIVE
def get_second_largest_number(l):
    if len(l) <= 1:
        return None
    largest = max(l)
    second_largest = None
    for number in l:
        if number != largest:
            if second_largest == None:
                second_largest = number
            else:
                second_largest = max(number, second_largest)
    return second_largest

# teacher's approach: single iteration

def get_second_largest_numer(l):
    largest = l[0]
    second = None
    for num in l:
        if num > largest:
            second = largest
            largest = num
        elif num != largest:
            if second == None or second < num:
                second = num
        # my approach
        # elif second == None and num < largest:
        #     second = num
        # elif second < num:
        #     second = num
    return second


if __name__ == "__main__":
    l = [20,20,20]
    print(get_second_largest_number(l))
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(get_second_largest_number(l))
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # print(get_second_largest_number(l))
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # print(get_second_largest_number(l))
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(get_second_largest_number(l))
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # print(get_second_largest_number(l))