# Diccionario. Pedir palabra, definición y permitir búsqueda
dicc = {}
continuar = True
while continuar:
    clave = input("Introduce la clave o 0 para salir\n")
    if clave != "0":
        desc = input("Introduce la descripción\n")
        dicc[clave] = desc
    else:
        continuar = False
continuar = True
while continuar:
    clave = input("Introduce la clave que buscas o 0 para salir\n")
    if clave != "0":
        print("Clave: {}, Descripción: {}".format(clave, dicc[clave]))
    else:
        continuar = False
