

def menor(num):
    '''Esta funcion permite quitar el digito menor 
    de un numero dado'''
    lista_numeros = []
    while num != 0:
        x = int(num % 10)
        num //= 10
        lista_numeros.append(x)
    lista_numeros.reverse()

    men = 10
    for i in range(len(lista_numeros)):
        if lista_numeros[i] < men:
            men = lista_numeros[i]

    print(men)

n = int(input())
for i in range(n):
    nu = int(input())
    menor(nu)