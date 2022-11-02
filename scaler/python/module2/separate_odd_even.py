def print_arr(arr):
    for i in arr:
        print(i, end=' ')
    print()
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for i in range(T):
        N = int(input())
        a = list(map(int, input().split()))
        odd_arr = []
        even_arr = []
        for i in a:
            if i%2==0:
                even_arr.append(i)
            else:
                odd_arr.append(i)
        print_arr(odd_arr)
        print_arr(even_arr)

    return 0

if __name__ == '__main__':
    main()