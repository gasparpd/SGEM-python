class Cajero:
    efectivo = 0
    billetes = None

    def __init__(self, efectivo, billetes):
        self.efectivo = efectivo
        self.billetes = billetes

    def dardinero(self, pedido, cliente):
        if pedido > self.efectivo:
            print("No se dispone de efectivo suficiente. El efectivo disponible es de: {}€".format(self.efectivo))
        else:
            if pedido > cliente.saldo:
                print("El efectivo pedido ({}) es superior al saldo disponible ({}€).".format(pedido, cliente.saldo))
            else:
                vuelta = self.calcularbilletes(pedido)
                if vuelta == pedido:
                    cliente.saldo -= pedido
                    self.efectivo -= pedido
                    print("Su saldo es de: {}€".format(cliente.saldo))
                else:
                    if pedido > vuelta > 0:
                        print("El cajero solo dispone de {}€. ¿Quiere este dinero? (SI/NO)".format(vuelta))
                        resp = input()
                        while resp != "SI" and resp != "NO" and resp != "si" and resp != "no":
                            print("Respuesta inválida")
                            print("El cajero solo dispone de {}€. ¿Quiere este dinero? (SI/NO)".format(vuelta))
                            resp = input()
                        if resp == "SI" or resp == "si":
                            cliente.saldo -= vuelta
                            self.efectivo -= vuelta
                            print("Su saldo es de: {}€".format(cliente.saldo))
                        else:
                            print("Disculpa las molestias")
                    else:
                        print("El cajero solo de los siguientes billetes:")
                        for i in range(len(self.billetes)):
                            valorbill = self.billetes[i][0]
                            totalbill = self.billetes[i][1]
                            if totalbill > 0:
                                print("Cajero dispone de {} billetes de {}€".format(totalbill, valorbill))

    def calcularbilletes(self, pedido):
        acumvuleta = 0
        for i in range(len(self.billetes)):
            valorbill = self.billetes[i][0]
            totalbill = self.billetes[i][1]
            billvuelta = 0
            if valorbill <= pedido:
                while totalbill > 0 and pedido - valorbill >= 0:
                    pedido -= valorbill
                    acumvuleta += valorbill
                    totalbill -= 1
                    billvuelta += 1
            self.billetes[i][1] = totalbill
            # print("Cajero dispone de {} billetes de {}€".format(totalbill, valorbill))
            print("Vuelta: {} bille/s de {}€".format(billvuelta, valorbill))
        return acumvuleta