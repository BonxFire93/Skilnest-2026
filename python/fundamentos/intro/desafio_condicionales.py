edad = 60
acompañante = True

if edad >= 18:
    print("Acceso permitido")

if edad == 16 and acompañante:
    print("Acceso permitido con adulto")

if edad == 17 and acompañante:
    print("Acceso permitido con adulto")

else:
    print("Acceso denegado")

if edad >= 60:
    print("Acceso permitido con descuento")