n = int(input())
c = 0
s = 0
r = 1

for i in range(0 , n):
    
    if c == r:
        c = 0
        if s == 0:
            s = 1
        else:
            s = 0
        r += 1
    c = c + 1    
    print(s, ',')

# 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0 ........