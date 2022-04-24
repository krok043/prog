#Generar para N términos: 1, 3, 3, 6, 5, 9, 7, 12, 9, 15, 11,

# 1 + 2
# 3 - 0
# 3 + 3
# 6 - 1
# 5 + 4
# 9 - 2
# 7 + 5
# 12 - 3
# 9 + 6
# 15 - 4

n = int(input())

s = 1
sum = 2
res = 0

op = True

for i in range(0, n):
    print(s)
    if op == True:
        s += sum
        sum += 1
        op = False
    else:
        s -= res
        res += 1
        op = True
    




