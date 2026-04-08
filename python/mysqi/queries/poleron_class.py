class Poleron:
    def __init__(self, color, material, modelo):
        self.color = color
        self.material = material
        self.modelo = modelo
        self.uso = False
        print(f"Se ha creado un poleron {self.color} de {self.material} de tipo {self.modelo}")
    def usar(self):
        self.uso = True
        print(f'El poleron {self.color} está siendo usado')
    def teñir(self, nuevo_color):
        print(f"el poleron {self.color} se tiñio de {nuevo_color}")
        self.color = nuevo_color

poleron1 = Poleron("Rosa", "Algodon", "Con Cierre y Gorro")
poleron2 = Poleron("Carmesi", "Poliester", "Hoddie")

print(poleron1.material)

poleron2.teñir("Morado")