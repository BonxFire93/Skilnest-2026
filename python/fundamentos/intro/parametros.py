def saludar(nombre="T/N", apellido="Y/N"):
    return "Hola", nombre + " " + apellido

def sumatoria_menos_longitud(lista):
    total_puntos = 0
    for elemento in lista :
        total_puntos += elemento
    return total_puntos - len(lista)
print(sumatoria_menos_longitud([10, 5, 3, 7]))