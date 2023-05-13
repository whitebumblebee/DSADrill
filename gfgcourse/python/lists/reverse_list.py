"""
Given a list, return its reverse list
"""

def reverse_list(l):

    i = 0
    j = len(l) - 1
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l

print(reverse_list([10,20,40,50]))