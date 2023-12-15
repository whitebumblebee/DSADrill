# for a given matrix n * m find the max columnwise sum

# the approach: find the sum for each column and return the max

matrix = [
    [3,8,9,2],
    [1,2,3,6],
    [4,10,11,13]
]
def calculate_max_sum_columnwise_on_matrix(matrix):
    N = len(matrix)
    M = len(matrix[0])
    max_sum = -100000000

    for i  in range(M):
        curr_sum = 0
        for j in range(N):
            curr_sum += matrix[j][i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

if __name__ == "__main__":
    print(calculate_max_sum_columnwise_on_matrix(matrix=matrix))
    

