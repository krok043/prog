#dado un x>100 mostrar los digitos repetidos 
#ejem si x=47527734
#mostrar 4,7
import math

n = int(input())
conD = 0
res = ""

nd = int(math.log10(n))
while n!=0 :
    d = n // 10**nd
    #si, existe digito repetido, eliminarlo
    n = n % 10**nd
    nd = nd - 1
    aux = n
    if auxd != 0:
        auxd = int(math.log10(aux))
        while aux != 0:
            dtemp = aux // 10**auxd
            if d == dtemp:
                conD = conD + 1
                break
                #n = n % 10**auxd
            aux = aux % 10**auxd
            auxd = auxd - 1
        if conD != 0:
            res = res + str(d) + ","
            conD = 0

print(res)





