def paths(matrix, i = 0, j = 0, lookup = None):
    lookup = {} if lookup is None else lookup

    n, m = len(matrix), len(matrix[0])
    if (i, j) in lookup:
        return lookup[(i, j)]
    elif i == n or j == m or matrix[i][j] == 1:
        lookup[(i, j)] = 0
        return lookup[(i,j)]
    elif i == n - 1 and j == m - 1:
        lookup[(i, j)] = 1
        return lookup[(i,j)]
    else:
        lookup[(i, j)] = paths(matrix, i + 1, j, lookup) + paths(matrix, i, j + 1, lookup)
        return lookup[(i,j)]

mat = []
for i in range(4):
    mat.append(list(map(int, input().split())))

print(paths(mat))