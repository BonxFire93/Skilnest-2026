class TarjetaCredito:
    banco = "Banco Estado"
    def __init__(self, limite_credito, saldo_pagar):
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        TarjetaCredito.todas_las_tarjetas.append(self)
    @classmethod
    def cambiar_banco(cls, nuevo_banco):
        cls.banco = nuevo_banco
    def todos_los_saldos(cls):
        total = 0
        for tarjeta in cls.todos_las_tarjetas:
            total += tarjeta.saldo_pagar
        return total