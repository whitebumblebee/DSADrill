def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    prime = False
    for i in range(2, A):
        if A%i == 0:
            prime = False
    prime = True
    if prime:
        print("YES")
    else:
        print("NO")
    return 0

if __name__ == '__main__':
    main()