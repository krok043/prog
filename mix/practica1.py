n = int(input())

while n < 1 or n > 1000:
    n = int(input())

b = True
d = 1

for i in range(n):
    for j in range(n):
        print(d, end='')
        if d == 0:
            d = 1
        else:
            d = 0
    if b == True:
        d = 0
        b = False
    else:
        d = 1
        b = True
    print()


