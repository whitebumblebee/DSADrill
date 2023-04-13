from copy import deepcopy
from collections import deque
def are_equal_stacks(input_first_stack, input_second_stack):
    first_stack = deepcopy(input_first_stack)
    second_stack = deepcopy(input_second_stack)
    try:
        if len(first_stack) == 0 and len(second_stack)==0:
            return True
        else:
            is_top_present_in_first_stack = first_stack[0]
            is_top_present_in_second_stack = second_stack[0]
            while first_stack and second_stack:
                top_of_first_stack = first_stack.pop()
                top_of_second_stack = second_stack.pop()
                if top_of_first_stack != top_of_second_stack:
                    return False
                else: 
                    continue
        return True
    except:
        print("exception")
        return False

if __name__ == '__main__':
    first_stack = deque([])
    second_stack = deque([])
    
    # for i in range(1,4):
    #     first_stack.append(i)
    #     second_stack.append(i)

    print(first_stack)
    print(second_stack)
    print(are_equal_stacks(first_stack, second_stack))