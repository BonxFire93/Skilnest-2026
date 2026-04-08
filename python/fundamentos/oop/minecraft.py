class Bloque:
    def __init__(self, nombre, dureza, herramienta):
        self.nombre = nombre
        self.dureza = dureza
        self.herramienta = herramienta
        self.roto = False

    def minar(self, herramienta_usada):
        if herramienta_usada == self.herramienta:
            self.roto = True
            return f"Obtuviste {self.nombre}!"
        return f"Necesitas {self.herramienta}"
    
piedra = Bloque("Piedra", 1.5, "pico")
madera = Bloque("Madera", 2.0, "hacha")
diamante = Bloque("Diamante", 5.0, "pico_hierro")
oro = Bloque("Oro", 4.0, "pico_hierro")
tierra = Bloque("Tierra", 0.5, "pala")
obsidiana = Bloque("Obsidiana", 8.0, "pico_diamante")

print(piedra.minar("pico"))
print(madera.minar("hacha"))
print(diamante.minar("pico_hierro"))
print(oro.minar("pico_hierro"))
print(tierra.minar("pala"))
print(obsidiana.minar("pico_diamante"))
print(f"¿Piedra rota? {piedra.roto}")