# CinetecaDigital, que debe incluir:

# Aributos:
# nombre
# ubicacion
# catalogo (diccionario de películas con sus detalles)
# peliculas_prestadas (diccionario que registra qué usuario tiene cada película)
# Métodos:
# agregar_pelicula(self, id_pelicula, titulo, director, genero, anio) agrega una película al catálogo.
# prestar_pelicula(self, id_pelicula, usuario) registra el préstamo de una película a un usuario.
# devolver_pelicula(self, id_pelicula) marca una película como disponible nuevamente.
# buscar_por_genero(self, genero) muestra las películas de un género específico.
# buscar_por_director(self, director) muestra las películas de un director específico.
# mostrar_catalogo_completo(self) muestra todas las películas en el catálogo con su estado.
# Realizar las siguientes pruebas con instancias:

# Crea una cineteca digital
# Agrega al menos 5 películas de diferentes géneros al catálogo
# Realiza 3 préstamos de películas a diferentes usuarios
# Devuelve una de las películas prestadas
# Busca las películas de un género específico
# Busca las películas de un director específico
# Muestra el catálogo completo con el estado de cada película

# peliculas_prestadas = [
#     {"pelicula id":1,
#      "usuario":"Antony"},
#      {"pelicua id":2,
#       "usuario":"Hugo"}]

# catalogo = [
#     {"id_pelicula":1,
#      "titulo":"El muñecop diabolico",
#      "director":"Don Mancini",
#      "genero":"suspenso",
#      "anio":1988,
#      "disponibilidad":True}]

class CinetecaDigital:
    def __init__(self, nombre, ubicacion,):
        self.nombre = nombre
        self.ubicacion = ubicacion
        #Catalogo es una lista de diccionarios
        self.catalogo = []
        #peliculas prestadas es una lista de diccionarios
        self.peliculas_prestadas = []

    def agregar_pelicula(self, id_pelicula, titulo, director, genero, anio):
#"""Agrega una nueva película al catálogo de la cineteca."""
        nueva_pelicula = {
            "id_pelicula" : id_pelicula,
            "titulo" : titulo,
            "director" : director,
            "genero" : genero,
            "anio" : anio,
            "disponibilidad" : True
         }
        self.catalogo.append(nueva_pelicula)
        return self

    def prestar_pelicula(self, id_pelicula, usuario):
#"""Registra el préstamo de una película a un usuario."""
        for pelicula in self.catalogo:
            if pelicula["id_pelicula"] == id_pelicula:
                if pelicula.disponibilidad == True:
                    pelicula.disponibilidad = False

                    pelicula_prestada = {
                        "id_pelicula" : id_pelicula,
                        "usuario" : usuario
                    }
                    self.peliculas_prestadas.append(pelicula_prestada)
                    print("la pelicula esta disponible")
                else:
                    print("la pelicula no esta disponible")
        print("El id ingresado no está en el catalogo")

    def devolver_pelicula(self, id_pelicula):
        for pelicula in self.catalogo:
            if pelicula ["id_pelicula"] == id_pelicula:
                pelicula["disponibilidad"] == True
                return self
        for pelicula in self.peliculas_prestadas:
            if pelicula ["id_pelicula"] == id_pelicula:
                self.peliculas_prestadas.remove(pelicula)
                return self
#"""Marca una película como disponible tras ser devuelta."""
        
    def buscar_por_genero(self, genero):
        nuevo_genero = []
        for pelicula in self.catalogo:
            if pelicula["genero"] == genero:
                pelicula["nuevo_genero"] == True
                return self
        self.catalogo.append(nuevo_genero)
        return self

#"""Muestra las películas disponibles de un género específico."""
      
    def buscar_por_director(self, director):
        for pelicula in self.catalogo:
            if pelicula["director"] == director:
                if pelicula.es == True:
                    pelicula.es = False
#"""Muestra las películas disponibles de un director específico."""

    @classmethod
    def mostrar_catalogo_completo(cls):
#"""Muestra el catálogo completo con el estado de cada película."""
        pass