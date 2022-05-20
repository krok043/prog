'''
Ejercicio base:
Genera un vector de n elementos con los numeros naturales
Ej:
    [1, 2, 3, 4, 5, ...]
'''

def gen_num(n):
    vec = []
    for i in range(1, n + 1):
        vec.append(i)
    return vec

n = int(input())
print(gen_num(n))