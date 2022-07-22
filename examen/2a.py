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
        n_list.append(a[i].capitalize())
    if i < len(b):
        n_list.append(b[i].capitalize())

print(n_list)