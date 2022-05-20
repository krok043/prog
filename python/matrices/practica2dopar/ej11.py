'''
Ej.11
Dados dos vectores de n elementos, sumar sus elementos 1 a 1
'''

v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

for i in range(len(v1)):
    print(v1[i] + v2[i], end = ' ')
