'''
Ej.9
Dado un vector X, invertir los números pares:
105 604 27 56 36 -> 105 406 27 65 63
'''

def mul_max(x):
    '''
        Calcula la cantidad de digitos y retorna 1*10^cdn
        donde:
            cdn = cantidad de digitos del numero
        Ej: 
            435 -> 100
            32 -> 10
            12424 -> 10000
            5 -> 1
    '''
    n = 1
    while x != 0:
        x //= 10
        n *= 10
    
    return n//10


def invertir(x):
    num_inv = 0
    mul = mul_max(x)
    while x != 0:
        a = (x % 10) * mul
        num_inv += a
        mul //= 10
        x //= 10
    return num_inv

n = list(map(int, input().split()))

for i in n:
    if i % 2 == 0:
        i = invertir(i)
    
    print(i, end=' ')
