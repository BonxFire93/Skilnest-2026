class Usuario:
    def __int__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.activo = True
#Crear usuario
u1 = Usuario("Sofia", "sofia@gmail.com", 17)
print(u1.nombre) #Sofía