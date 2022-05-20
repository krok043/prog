#Hay dos formas de resolver:
#1ra: Como caracteres
def medio_1ra(num):
    l = len(num)
    m = l // 2
    if l % 2 == 0:
        print(num[m-1:m+1])
    else:
        print(num[m])

#2da: Como numeros
def medio_2da(num):
    num = int(num)
    lista_numeros = []
    while num != 0:
        x = int(num % 10)
        num //= 10
        lista_numeros.append(x)
    
    lista_numeros.reverse()
    l = len(lista_numeros)
    m = l // 2

    if l % 2 == 0:
        print(f'{lista_numeros[m-1]}{lista_numeros[m]}')
    else:
        print(lista_numeros[m])



n = int(input())
for i in range(n):
    nu = input()
    #medio_1ra(nu)
    medio_2da(nu)
