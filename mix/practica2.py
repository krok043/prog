n = int(input())

while n < 1 or n > 100:
    n = int(input())

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

l_ma = []
l_me = []

def pos_mayor(v):
    pos = -1
    temp = 0
    for i in range(len(v)):
        if temp < v[i] and i not in l_ma:
            # l_ma.append(i)
            temp = v[i]
            pos = i
    l_ma.append(pos)
    return pos

def pos_menor(v):
    temp = 9999999
    pos = -1
    for i in range(len(v)):
        if temp > v[i] and i not in l_me:
            #l_me.append(i)
            temp = v[i]
            pos = i
    l_me.append(pos)
    return pos

#Reordenar A (2)
for i in range(n):
    pos_mayor(b)
    pos_menor(a)


t = a.copy()
#t = a
c = 0
for i in l_me:
    a[i] = t[l_ma[c]]
    c += 1

    
    
print(l_me)
print(l_ma)
print(t)

# s = 0
# for i in range(i):
#     s = s + (a[i] * b[i])

# print(s)