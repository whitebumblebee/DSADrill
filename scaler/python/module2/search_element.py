def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for i in range(T):
        A = list(map(int, input().split()))
        B = int(input())
        flag = True
        for number in A:
            if number == B:
                print(1)
                flag = False
                break
        if flag:
            print(0)


if __name__ == '__main__':
    main()