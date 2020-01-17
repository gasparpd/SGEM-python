from .Cliente import Cliente


class Cajero:
    efectivo = 1000
    billetes = [[50, 10], [20, 20], [10, 10]]

    def __init__(self, efectivo, billetes):
        self.efectivo = efectivo
        self.billetes = billetes

    def dardinero(self, pedido, cliente):
        if pedido > self.efectivo:
            print("No se dispone de efectivo suficiente. El efectivo disponible es: " + self.efectivo)
        else:
            if pedido > cliente.saldo:
                print("El efectivo pedido ({}) es superior al saldo disponible en su cuenta ({})€.")
            else:
                self.calcularbilletes(pedido)

    def calcularbilletes(self, pedido):
        acumvuelta = 0
        for i in range(self.billetes.len()):
            valor = self.billetes[i][0]
            nbill = self.billetes[i][1]
            if valor > pedido:
            else:
                while nbill > 0

c = Cliente("1111111X", 750)
c2 = Cliente("2222222X", 5500)