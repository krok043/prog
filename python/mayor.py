n = int(input())

if n >= 1 and n <= 100000:
    for i in range(1, n):
        x = int(input())
        while x < 100 and x > 1000000000:
            x = int(input())

        t = x
        c = 0

        while t != 0:
            t = int(t / 10)
            c += 1
        
        mul = 10 ** (c - 1)
        res = x / mul
        