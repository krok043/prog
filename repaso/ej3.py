def contarDigito(n):
    c = 0
    while n > 0:
        n = n // 10
        c = c + 1
    return c        


def inversorDigito(n):
    invertido = 0
    mul = 10 ** (contarDigito(n)-1)

    while n > 0:
        r = n % 10
        n = n // 10
        invertido = invertido + (r * mul)
        mul = mul // 10

    return invertido


def digitoMedio(n):
    cd = contarDigito(n)
    r = 0
    if cd % 2 == 0:
        mul = 10
        mid = (cd // 2)
        for i in range(mid+1):
            dig = n % 10
            if i >= mid-1:
                r = r + (dig * mul)
                mul = mul // 10
            n = n // 10
    else:
        mid = (cd // 2) + 1
        for i in range(mid):
            r = n % 10
            n = n // 10
    return r

x = [int(i) for i in input().split()]

xinv = []

for i in range(len(x)):
    xinv.append(inversorDigito(x[i]))

xmedio = []

for i in range(len(x)):
    xmedio.append(digitoMedio(xinv[i]))

print(xinv)
print(xmedio)