n = int(input())
c = 1

while c <= n:
    b = True

    #3
    num = int(input())
    for i in range(2, num):
        if num % i == 0:
            b = False
            break

    if b:
        t = "{:.40f}".format(1 / num)
        dig = t.split('.')[1]
        x = ''
        for j in dig:
            x = x + j + ' '
        print(num, ":", x)
    else:
        print(num, ": -1")
    
    c = c + 1