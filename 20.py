import libmath

x = int(input())

if x > 100:
    print(libmath.first_digit(x))
    print(libmath.last_digit(x))
    print(libmath.first_digit(101))