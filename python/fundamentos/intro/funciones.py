def NombreFuncion (Parametro1, Parametro2):
    #acciones que se van a ejecutar cuando invoque la funcion
    print(Parametro1)
    print(Parametro2)

NombreFuncion("Pepe", "Marcelo")


def sumarTresNumeros (num1, num2, num3):
    total = num1 + num2 + num3
    return total
print(sumarTresNumeros(3, 7, 10))

superTotal = sumarTresNumeros(3, 7, 10) + 5
print(superTotal)