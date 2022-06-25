def mayor(n1, n2,  n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    elif n3 > n1:
        return n3


v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))

m = mayor(len(v1), len(v2), len(v3))

v4 = []

p = 0

for i in range(m):
    if p < len(v1):
        v4.append(v1[p])

    if p < len(v2):
        v4.append(v2[p])

    if p < len(v3):
        v4.append(v3[p])

    p += 1

print(v4)
