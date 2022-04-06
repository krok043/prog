numeros = input()

n1, n2, n3 = numeros.split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
elif n2 > n3:
    print(n2)
else:
    print(n3)