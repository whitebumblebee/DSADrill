def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N, *arr = list(map(int, input().split()))
    min_val = 1000000000
    max_val = -100000000
    for num in arr:
        if num >= max_val:
            max_val = num
        if num <= min_val:
            min_val = num
    print(max_val, min_val)

if __name__ == '__main__':
    main()