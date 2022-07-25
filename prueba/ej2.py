n = int(input())
l = []

for i in range(n):
    l.append(input())

def rotar(v, j):
    return v[j:] + v[:j]

if n % 2 == 0:
    l = l[::-1]
else:
    j = -1
    l = l[-1:] + l[:-1]
print(l)

