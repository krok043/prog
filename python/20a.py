def  ultimo(n):

    digito = n % 10

    return digito    

def primero(n):
    while n > 10:        
        n = int(n / 10)
    return n

x = int(input())

prim = primero(x)
digito = ultimo(x)

if x > 100:
    print(prim,digito)