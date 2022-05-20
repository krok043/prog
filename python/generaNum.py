n = int(input())
i = 1
suma = True


c = 1
while c <= 10:
    print(i, ", ")
    if suma:
        i = i + 1
    else:
        i = i - 1    
    
    if i == n:
        suma = False
    
    if i == 1:
        suma = True

    
    c += 1