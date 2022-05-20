n,m = (2, 4)
matriz = []

for i in range(n):
    fila = []
    for j in range(m):
        fila.append('*')
    matriz.append(fila)

for i in range(n):
    print(*i)