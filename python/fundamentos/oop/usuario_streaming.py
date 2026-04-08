class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion):
      self.nombre = nombre
      self.email = email
      self.suscripcion = suscripcion
      self.lista_reproduccion = []
      print(f"se ha crado el usuario de {nombre}")
   def agregar_a_lista(self, titulo):
      self.lista_reproduccion.append(titulo)
      print(f"{titulo} se ha agregado a la lista de reproduccion")
      return self
   def ver_contenido(self):
      for elemento in self.lista_reproduccion:
         print(f"Se esta reproduciendo {elemento}")
      return self
   def cambiar_suscripcion(self, nueva_suscripcion):
      self.suscripcion = nueva_suscripcion
      print(f"El usuario {self.nombre} ha cambiaso de suscrpcion a {nueva_suscripcion}")
      return self
   def mostrar_info_usuario(self):
      print(f"Usuario: {self.nombre}, Email: {self.email}, Suscripcion: {self.suscripcion}")
      print("Lista de Reproduccion")
      print(self.lista_reproduccion)
      return self

u1 = UsuarioStreaming("WAZAA2.0", "elwazamaspro@gmail.com", "Gratis")
u2 = UsuarioStreaming("ElMasKp1to", "hola@gmail.com", "Premium")
u1.agregar_a_lista("insepcion").agregar_a_lista("Futurama").agregar_a_lista("The King Lion")
u2.agregar_a_lista("Shrek")
u1.mostrar_info_usuario()