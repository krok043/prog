usuario = 'juan'
password = 'perez'

con = 1

while con <= 3:
    u = input("Ingrese usuario: ")
    p = input("Ingrese password: ")

    if usuario == u:
        if password == p:
            print("Bienvenido Juan")
            break
        else:
            print("Password incorrecto")
    else:
        print("Usuario incorrecto")
    con = con + 1

if con > 3:
    print("Superaste los 3 intentos")