def last_digit(n):
    return n % 10

def first_digit(n):
    while n >= 10:
        n = int(n / 10)
    return n

def minor_digit(n):
    menor = 99999999999999999999
    while n > 0:
        r = n % 10
        if r < menor:
            menor = r
        n = int(n / 10)

    return menor

def remove_digit(d):
    #Algoritmo para eliminar un digito de un numero dado
    pass