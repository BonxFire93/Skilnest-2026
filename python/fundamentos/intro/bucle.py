#1 argumento (Fin)
for i in range(4):
	print(i)
	print("hola") #dentro del codgio, se imprimira dentro de tal
print("bye") #fuera del codigo, no se imprimira dentro de tal

print("------------------------------------------------------")

#2 argumentos (inicio, fin)
for i in range(2, 6):
	print(i)

print("------------------------------------------------------")

#3 argumentos (inicio, fin, paso)
for i in range(2, 10, 3):
	print(i)

print("------------------------------------------------------")

for i in range(0, 15, 3):
	print(i)

print("------------------------------------------------------")

for i in range(20, 0, -5):
	print(i)

print("------------------------------------------------------")

for letra in "Python":
	if letra == "i":
		print("Python se escribe con Y")
	else:
		print("Muy bien, no olvidaste la Y")
		
print("------------------------------------------------------")

lista = ["Lapiz", "Papel", "Plumones"]
for indice in range(len(lista)):
	print(indice, lista[indice])
	
for elemento in lista:
	print(elemento)

print("------------------------------------------------------")

estudiante = {"nombre": "Gonzalo", "curso": "Python"}
for clave in estudiante:
	print(clave)
#Imprime: nombre, curso

estudiante = {"nombre": "Gonzalo", "curso": "Python"}
for clave in estudiante:
	print(estudiante[clave])
#imprime: Gonzalo, Python

print("------------------------------------------------------")

platillos_tipicos = {"Mexico":"Tacos", "Colombia":"Ajiaco", "Costa Rica":"Casado"}
print(platillos_tipicos)

#otra forma de iterar a traves de las claves
for clave in  platillos_tipicos.keys():
	print(clave)
#imprime: mexico, colombia, costa rica

#iteramos a traves de los valores
for valor in platillos_tipicos.values():
	print(valor)
#imprime: tacos, ajiaco, casado

#iteramos a travez de los elementos (clave-valor)
for clave, valor in platillos_tipicos.items():
	print(clave, "=", valor)
#imprime: mexico = tacos, colombia = ajiaco, costa rica = casado

print("------------------------------------------------------")

num = 0

while num < 4:
	print("bucle while -", num)
	num += 1
#imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

print("------------------------------------------------------")

for letra in "detente":
	if letra == "n":
		break
	print(letra)
#Imprime: d, e, t, e

print("------------------------------------------------------")

for letra in "detente":
	if letra == "n":
		continue
	print(letra)
#Imprime: d, e, t, e, t, e
