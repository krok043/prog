def gen_ciclos(n):
    c_ciclos = 1

    while n>1:
        if n%2==0:
            n=n//2
        else:
            n=(n*3)+1
        c_ciclos += 1

    return c_ciclos

a = int(input('Ingresa a: '))
b = int(input('Ingresa b: '))

mayor = 0

if a < b:
    for i in range(a, b+1):
        t = gen_ciclos(i)
        if t > mayor:
            mayor = t

print(mayor)