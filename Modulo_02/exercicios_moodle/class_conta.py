class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = float(saldo_inicial)

    def depositar(self, valor):
        self.saldo += float(valor)
        print(f"Depósito de R$ {valor:.2f} feito. Saldo agora: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        valor = float(valor)
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque ok.")
            print(f"Saldo restante: R$ {self.saldo:.2f}")
        else:
            print("Não tem saldo suficiente.")

conta = ContaBancaria("Ana", 100)
conta.depositar(50)
conta.sacar(30)
conta.sacar(200)