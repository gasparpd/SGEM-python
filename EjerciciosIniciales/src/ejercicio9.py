#Ejercicio 9
'''
d={}
d["clave1"] = "valor1"
d["clave2"] = "valor2"

print(d["clave1"])

for clave in d.keys():
    print("{}:{}".format(clave, d[clave]))
'''

d = {}
continuar = True
while continuar:
    print("Introduce la palabra clave o '1' para salir.")
    clave = input()
    if clave == "1":
        continuar = False
    else:
        print("Introduce la definición.")
        defin = input()
        d[clave] = defin
print("Diccionario completo.")
continuar = True
while continuar:
    print("¿Qué palabra desea buscar?\nIntroduce '1' para dejar de buscar.")
    p = input()
    if p == "1":
        continuar = False
    else:
        print("Clave: {}, Definición: {}".format(p, d[p]))
print("Final del programa")