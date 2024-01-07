# def f(N):
#     if N < 1:
#         return
#     f(N-1)
#     print(N)

# def main():
#     N = int(input())
#     f(N)

# if __name__ == '__main__':
#     main()
#     exit(0)

# without backtrack
    
# def f(N):
#     if N < 1:
#         return
#     print(N)
#     f(N-1)

# def main():
#     N = int(input())
#     f(N)

# main()

# Backtrack for printing  N to 1

def f(i, N):
    if i > N:
        return
    f(i+1, N)
    print(i)

N = int(input())
f(1, N)




