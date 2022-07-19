
n = int(input())
x = int(input())

s = 0
b = False

for i in range(1, n+1, 1):
    expo = 2 ** i
    deno = 1
    for j in range(1, i * 2, 1):
        deno = deno * j

    if b == False:
        s = s - (x ** expo ) / deno
        b = True
    else:
        s = s + (x ** expo ) / deno
        b = False

print(s)