class Jugador:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.__vida = 20
        self.__hambre = 20
    
    @property
    def vida(self):
        return self.__vida
    
    def recibir_daño(self, cantidad):
        self.__vida = max(0, self.__vida - cantidad)
        if self.__vida == 0:
            return f"{self.nombre} ha muerto!"
        return f"{self.nombre} - vida: {self.__vida}/20"
    
    def comer(self, comida):
        recupera = {"manzana" : 4, "carne" : 8, "pan" : 5}
        if comida in recupera:
            self.__hambre = min(20, self.__hambre + recupera[comida])
            return f"Hambre: {self.__hambre}/20"
        return f"{comida} no es comestible"
    
steve = Jugador("Steve")
print(steve.recibir_daño(5))
print(steve.vida)
print(steve.comer("carne"))