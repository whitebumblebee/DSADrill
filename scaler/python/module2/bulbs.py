#  My approach


def bulbs(self, A):
    switch_changes = 0
    for num in A:
        if num == 0:
            if switch_changes % 2 == 0:
                switch_changes += 1
            else:
                continue
        if num == 1:
            if switch_changes % 2 != 0:
                switch_changes += 1
            else:
                continue
    return switch_changes
     
#  approach using carry forward as it was the question on carry forward
def bulbs(A):
    count = 0
    for i in A:
        state = i
        if count % 2 == 0:
            state = i
        else:
            state = 1 - i
        if state == 0:
            count += 1

    return count
          

