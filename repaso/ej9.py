
n,m = map(int, input().split())

c = 1
s = 0
mat = []

for i in range(n):
    fila = []
    for j in range(m):
        s = s + c
        fila.append(s)
        s += n
    c = c + 1
    s = 0
    mat.append(fila)
    

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=' ')
    print()