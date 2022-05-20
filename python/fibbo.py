from curses.ascii import NL


def fibo(n):
    seriefibo = []
    s1 = 0
    s2 = 1
    s3 = 0
    seriefibo.append(s1)
    seriefibo.append(s2)
    for i in range(2, n):
        s3 = s1 + s2
        seriefibo.append(s3)
        s1 = s2
        s2 = s3
    return seriefibo


a = int(input())
b = int(input())
c = int(input())

print(fibo(a))
print(fibo(b))
print(fibo(c))