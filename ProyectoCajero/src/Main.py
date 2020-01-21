from src.cajero import Cajero
from src.Cliente import Cliente

c = Cliente("1111X", 750)
c2 = Cliente("2222X", 5500)

efectivo = 1000
billetes = [[50, 3], [20, 3], [10, 0]]
salir = False
while not salir:
    print("Introduce el PIN (0000A)")
    pin = input()
    while pin != "1111X" and pin != "2222X":
        print("El pin nos se corresponde con ningún cliente.\nIntroduce el PIN (0000A)")
        pin = input()
    print("Introduce el efectivo que quieras sacar.")
    pedido = int(input())
    caj = Cajero(efectivo, billetes)
    caj.dardinero(pedido, c)
    print("Introduce 0 si quieres salir del programa")
    entrada = input()
    if entrada == "0":
        salir = True