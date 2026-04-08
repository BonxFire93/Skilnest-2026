class Usuario:
    def __init__(self, nombre, email, edad, activo):
        self.nombreU = nombre
        self.emailU = email
        self.edadU = edad
        self.activoU = activo

info = Usuario("Antony", "holaloko@gmail.com", 17, (False))
info = Usuario("Catalina", "wazaa@gmail.com", 18, (True))
info = Usuario("Hugo", "ilovemusic@gmail.com", 17, (False))

print(info)

class Poleron:
    def __init__(self, color, material, modelo):
        self.color = color
        self.material = material
        self.modelo = modelo
        self.uso = False
        print(f"Se ha creado un poleron {self.color} de {self.material} de tipo {self.material}")
    def usar(self):
        self.uso = True
        print(f'El poleron {self.color} está siendo usado')
    def teñir(self, nuevo_color):
        print(f"el poleron {self.color} se tiñio de {nuevo_color}")
        self.color = nuevo_color

poleron1 = Poleron("Rosa", "Algodon", "Con Cierre y Gorro")
