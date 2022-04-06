n = int(input())
a = n
c = 0
while n != 0:
    n = int(n / 10)
    c += 1

mul = 1 * 10 ** (c-1)
res = a / mul


print(int(res))
