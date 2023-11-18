def solve(self, A):
        maxi = max(A)
        mini = min(A)
        max_i = min_i = None
        current_min = 100000000000
        for i in range(len(A)):
            if A[i] == maxi:
                max_i = i
                # print("max i", max_i)
                if max_i is not None and min_i is not None:
                    # print("reached 3")
                    length_of_subarr = abs(max_i - min_i) + 1
                    if length_of_subarr < current_min:
                        # print("reached 1")
                        current_min = length_of_subarr
            if A[i] == mini:
                min_i = i
                print("min i",min_i)
                print("max i 2", max_i)
                if max_i is not None and min_i is not None:
                    print("reached 4")
                    length_of_subarr = abs(max_i - min_i) + 1
                    if length_of_subarr < current_min:

                        print("reached 2")
                        current_min = length_of_subarr
        # print(f"curr min {current_min}")
        return current_min

print(solve("self", [834,563,606,221,165]))