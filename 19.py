# S = Sumatoria desde 1 hasta n de la serie (2*i^2)/i
n = int(input())

s = 0

for i in range(1, n+1):
    s = s + ((2*(i**2))/5)

print(s)
