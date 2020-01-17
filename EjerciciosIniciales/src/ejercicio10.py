"""
Cálculo de los años bisiestos posteriores a 2016.
Para ser bisiesto debe ser divisible por 4. Execto aquellos que son divisibles entre 100
pero no entre 400
"""
nbis = 0
inicio = 2016
while nbis < 20:
    if inicio % 4 == 0 or (inicio % 100 == 0 and inicio % 400 == 0):
            print(str(inicio) + " es bisiesto.")
            nbis += 1
    #else:
    #   print(str(inicio) + " no es bisiesto.")
    inicio += 1