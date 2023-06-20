matrix = []

n,m = input().split()

for i in range(int(n)):
    matrix.append(list(map(int,input().split())))
    
def min_ways(matrix, i=0, j=0, lookup = None):
    lookup = {} if lookup is None else lookup
    n = len(matrix)
    m = len(matrix[0])
    
    if (i, j) in lookup:
        return lookup[(i,j)]
    if i == n - 1 and j == m - 1:
        lookup[(i, j)] = matrix[i][j]
        return lookup[(i, j)]
    elif i == n-1:
        lookup[(i, j)] =  matrix[i][j] + min_ways(matrix, i, j+1)
        return lookup[(i, j)]
    elif j == m-1:
        lookup[(i, j)] =  matrix[i][j] + min_ways(matrix, i+1, j)
        return lookup[(i, j)]
    else:
        lookup[(i, j)] =  matrix[i][j] + min(min_ways(matrix, i+1,j), min_ways(matrix,i,j+1))
        return lookup[(i, j)]
        

print(min_ways(matrix))
        
        
