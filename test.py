n = int(input())

m = ''
c = 0

if 1 <= n and n <= 1000000:
    for i in range(0, n):
        x = int(input())
        while 100 > x and x > 1000000000:
            x = int(input())
        
        t = x 
        con = 0
        while t!= 0:
            t=int(t / 10)     
            con = con + 1
        mul = 10**(con-1)
        res = int(x/mul)
        
        b = True

        for i in range(2, res):
            if res % i == 0:
                b = False
                break
        
        if b:
            m = m + str(res)
            
        else:
            m = m + '0'
            c += 1

print('Numero resultante = ', int(m))
print('Se leyeron', c, 'numeros que no tenian primer digito primo')