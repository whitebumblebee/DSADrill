def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N, *arr = list(map(int, input().split()))
    k = int(input())
    aux_arr = [0]*N
    for i in range(N):
        new_index = i + k%N
        if new_index >= N:
            aux_arr[new_index-N] = arr[i]
        else:
            aux_arr[new_index] = arr[i]
    for i in aux_arr:
        print(i, end=' ')


    return 0

if __name__ == '__main__':
    main()