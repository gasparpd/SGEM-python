#Ejercicio 9
d={}
d["clave1"] = "valor1"
d["clave2"] = "valor2"

print(d["clave1"])

for clave in d.keys():
    print("{}:{}".format(clave, d[clave]))