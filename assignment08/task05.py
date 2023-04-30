def rotate(n_rows, m_columns, matrix):
    for i in range(m_columns):
        for j in range(n_rows - 1, -1, -1):
            print(matrix[j][i], end=" ")
        print()


n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
array = [[int(j) for j in input().split()] for i in range(n)]
rotate(n, m, array)
