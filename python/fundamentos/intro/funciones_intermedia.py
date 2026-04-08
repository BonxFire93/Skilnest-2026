# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600
print(puntajes)
print()

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"
print(streamers)
print()

# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)

# Coordenadas de la sede de un torneo internacional
ubicacion = [{"latitud": 34.052235, "longitud": -118.243683}]
ubicacion[0]["latitud"] = 40.712776
print(ubicacion)
print()

def iterar_diccionario(lista):
    for dic in lista:
        salida = ", ".join([f"{clave} - {valor}" for clave, valor in dic.items()])
        print(salida)

iterar_diccionario(streamers)

def obtener_valores(clave, lista):
    for dic in lista:
        if clave in dic:
            print(dic[clave])

obtener_valores("nombre", streamers)
print()

categorias = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

def mostrar_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print()
mostrar_informacion(categorias)