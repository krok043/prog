x = int(input())

res = ""

while(x<100):
    x = int(input())
while(x!=0):
    d = x%10
    x = x//10
    y=x
    c=1
    while(y!=0):
        d1 = y%10
        y=y//10
        if(d==d1):
            c=c+1
        if(c>=2):
            if str(d) not in res:
                res = res + str(d)
                print(d, end=',')
                break