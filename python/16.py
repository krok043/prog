x = int(input())

#s = ((x ** 1) / 5) + ((x ** 3) / 10) + ((x ** 5) / 15) + ((x ** 7) / 20)

s = 0
e = 1
d = 5

for i in range(0, 4):
    s = s + (x ** e)/d
    e = e + 2
    d = d + 5

print(s)