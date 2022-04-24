

num = int(input())
primo = True
for n in range(2, num):
    if num % n == 0:
        print("No es primo", n, "es divisor")
        primo = False
print("Es primo")



n = (1 * 10 ** 40) / 19
n1 = "{:.40f}".format(1 / 19)

print(n)
print(n1)