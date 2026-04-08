"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

for nivel in range(0, 101):
    print("Nivel -", (nivel))
print("------------------------------------------------------")
# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

for potenciadores in range(2, 501, 2):
    print("power up -", (potenciadores))
print("------------------------------------------------------")
# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

for nivel in range(0, 101):
    print("Nivel -", (nivel))
if nivel % 10 == 5:
    print("Nivel -", (nivel))
print("------------------------------------------------------")
# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

num1 = 0
num2 = 500000
sumar = (num1, num2)
for sumar in range (0, + 500001):
    print("total -", (sumar))
print("------------------------------------------------------")
# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

for años in range(2024, -2, -3):
    print("Año -", (años))
print("------------------------------------------------------")
# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

inicio = 3
fin = 10
salto = 2
if inicio == 3:
    print("nivel - 4", "nivel - 6", "nivel - 8", "nivel-10")
if fin == 10:
    print("nivel - 4", "nivel - 6", "nivel - 8", "nivel-10")
if salto == 2:
    print("nivel - 4", "nivel - 6", "nivel - 8", "nivel-10")
# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10