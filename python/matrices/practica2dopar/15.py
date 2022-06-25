x = input()
v1 = []
v2 = []

for i in range(len(x)):
    n = int(x[i])
    if n % 2 == 0:
        v2.append(n)
    else:
        v1.append(n)

print(v1, v2)
