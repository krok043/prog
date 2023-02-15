class Auto:
    def __init__(self):
        self.anio = 95
        self.color = "Rojo"
        self.marca = "Nissan"
        self.model = "Ipsum"

    def saludo(self):
        self.nombre_auto = "GG"
        print(self.nombre_auto + " te manda un saludo")

a1 = Auto()

a1.saludo()

a1.cantidad_puertas = 4

print(a1.cantidad_puertas)