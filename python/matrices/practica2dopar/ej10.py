'''
Ej.10
Dado un vector de n elementos, promediar los elementos primos
'''

def primo(n):
    prim = True
    for i in range(2, n):
        if n % i == 0:            
            primo = False
    return prim


v = list(map(int, input().split()))
primos = []
sum = 0
for i in v:
    if primo(i): primos.append(i)

for i in primos:
    sum += i

print(sum / len(primos))
