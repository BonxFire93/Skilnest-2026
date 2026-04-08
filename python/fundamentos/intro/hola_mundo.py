# 1. Imprime "Hola, mundo"
#    Reemplaza el comentario con el código necesario para que, al ejecutar,
#    aparezca en pantalla la frase "Hola, mundo".
#    Ejemplo de uso: print("Mensaje")
# ---------------------------------------------------------------
print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
#    a) Concatenación usando comas
#    b) Concatenación usando +
# ---------------------------------------------------------------
nombre = "Antony"
print("Hola", nombre)
print("Hola" + nombre)

# 3. Imprime "Hola 156!" con el número en una variable
#    a) Usando comas
#    b) Usando + (esto podría dar error si no conviertes el número a str)
# ---------------------------------------------------------------
numero = 69
print("mi numero de la suerte es", numero)
print("mi numero de la suerte es" + str(numero))

# 4. Imprime "Me encanta comer X e Y" con dos de tus comidas favoritas
#    a) Usando .format()
#    b) Usando f-strings
# ---------------------------------------------------------------
comida1 = "Papas Rellenas"
comida2 = "Pizza"
print(f"Mis gustos son {comida1} y {comida2}")

print("Mis gustos son {} y {}".format(comida1, comida2))