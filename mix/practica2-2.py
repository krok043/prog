import sys
def orden(a,n):
    for i in range(n):
        for j in range(i+1,n):
            if a[j] < a[i]:
                aux = a[i]
                a[i] = a[j]
                a[j] = aux
def orden2(a,n):
    for i in range(n):
        for j in range(i+1,n):
            if a[j] > a[i]:
                aux = a[i]
                a[i] = a[j]
                a[j] = aux
for linea in sys.stdin:
    n=int(linea)
    a=input().split()
    b=input().split()
    a1=[0]*n
    b1=[0]*n
    s=0
    for i in range(n):
        a1[i]=int(a[i])
        b1[i]=int(b[i])
    orden(a1,n)
    orden2(b1,n)
    for i in range(n):
        s+= a1[i]*b1[i]
    print(s)