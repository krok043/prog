def baila(texto):
    n_te = ""
    b = True
    for i in texto:
        if b:
            n_te += str.upper(i)
            b = False
        else:
            n_te += i
            b = True
    return n_te

a = [i for i in input().split()]
b = [i for i in input().split()]

max = 0
if len(a) > len(b):
    max = len(a)
else:
    max = len(b)

n_list = []

for i in range(max):
    if i < len(a):
        n_list.append(baila(a[i]))
    else:
        pass
    if i < len(b):
        n_list.append(baila(b[i]))
    else:
        pass

print(n_list)