#Generar para N términos: 0, 0, 2, 2, 4, 4, 6, 6, 8, 8, …
n = int(input())

c = 0
s = 0

for i in range(0, n):
    if c == 2:
        c = 0
        s = s + 2

    c = c + 1
    print(s, ', ')

