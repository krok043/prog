def mayor_num(vec,n):
    t = -1000000001
    for i in range(n):
        if t < vec[i]:
            t=vec[i]
    return t

n,m=map(int,input().split())
matriz = []
vec = []

for i in range(n):
    lista = []
    lista=[int(p) for p in input().split()]
    matriz.append(lista)
    vec.append(mayor_num(lista,m))

print("matriz de entrada:")
for o in matriz:
    print(*o)
print("vector de salida:")
print(*vec)