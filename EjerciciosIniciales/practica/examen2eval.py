clave = "STOP"
continuar = True
cont = 0
while continuar:
    pal = input("Introduce una palabra. (STOP para salir)\n")
    if pal == clave:
        continuar = False
    else:
        cont += 1
print("Palabras introducidas: {}".format(cont))
