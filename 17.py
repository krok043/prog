#Hallar: S = x^2/2! – x^4/4! + x^8/6! – x^16/8!
x = int(input())

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i

    return f
# s = (x**2/(1*2)) - (x**4/(1*2*3*4)) + (x**8/(1*2*3*4*5*6)) - (x**16/(1*2*3*4*5*6*7*8))

s = 0
e = 2
d = 2
for i in range(0, 4):
    s = s + (x ** e)/factorial(d)
    d = d + 2
    e = e * 2

print(s)


