# 10 pkt
def create_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(i * n + j + 1)
    return matrix


# 30 pkt
def get_col_min(matrix, col):
    min = matrix[0][col]
    index = 0
    for i in range(1, len(matrix)):
        if matrix[i][col] < min:
            min = matrix[i][col]
            index = i
    return min, index


# 30 pkt
def get_col_max(matrix, col):
    max = matrix[0][col]
    index = 0
    for i in range(1, len(matrix)):
        if matrix[i][col] > max:
            max = matrix[i][col]
            index = i
    return max, index


def get_min_max_for_each_col(matrix):
    min_max = []
    for i in range(len(matrix)):
        min_max.append(get_col_min(matrix, i))
        min_max.append(get_col_max(matrix, i))
    return min_max


def sum_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


# 30 pkt
def sort_rows_reverse(matrix):
    for i in range(len(matrix)):
        matrix[i].sort(reverse=True)
    return matrix


my_matrix = create_matrix(3)
sum = 0
print(my_matrix)

print("Minimum i maximum dla kolumn: ", get_min_max_for_each_col(my_matrix))

sum = sum_diagonal(my_matrix)
print("Suma przekątnej: ", sum)

print("Posortowane wiersze: ", sort_rows_reverse(my_matrix))
