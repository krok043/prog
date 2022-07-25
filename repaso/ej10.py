def mayus(n,m):
    for i in range(n):
        for j in range(m):
            print(matriz[i][j].upper(), end=' ')
        print()

n,m = map(int,input().split())
matriz=[]
for i in range(n):
    fila = []

    for j in range(m):
        fila.append(input())
    matriz.append(fila)

mayus(n,m)