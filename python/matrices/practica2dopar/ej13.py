def fibo(n1, n2):
    n3 = n1 + n2
    return n1, n2, n3

# def primo(n):
#     esPrimo = True
#     for i in range(2, n):
#         if n % i == 0:
#             esPrimo = False
#     return esPrimo

n = int(input())
vector = []

#variables semilla para fibo
s1 = 0
s2 = 1


for i in range(n):
    if i % 2 == 0:
        #fibo        
        s1, s2, s3 = fibo(s1, s2)
    else:
        #primo
        pass
    

    
#N = 6
#        i 0  1  2  3  4  5
#vector = [1, 0, 3, 1, 5, 1] #length(6)