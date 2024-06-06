def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(3, 5, 11)
result2 = get_matrix(4, 4, 20)
result3 = get_matrix(1, 9, 17)
print(result1)
print(result2)
print(result3)
