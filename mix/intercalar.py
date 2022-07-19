#intercalar 2 numeros de distinto tamaño
#x 45 y 7635 z475635
#

import math

x = int(input())
y = int(input())

xd = int(math.log10(x))
yd = int(math.log10(y)) #OJO,  esta linea me devuelve la cantidad de digitos - 1

mayor = 0

if xd > yd:
    mayor = x
    dmayor = xd
    
else:
    mayor = y
    dmayor = yd

n = 0

while mayor != 0:

    if xd >= 0:
        d = x // 10**xd
        n = n * 10 + d

    if yd >= 0:
        d = y // 10**yd
        n = n * 10 + d
    
    x = x % 10**xd
    y = y % 10**yd
    xd = xd - 1
    yd = yd - 1
    mayor = mayor % 10**dmayor
    dmayor = dmayor - 1
print(n)

