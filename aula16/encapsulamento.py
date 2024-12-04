class ContaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.__saldo = saldo

    def exibir_saldo(self):
        # self.__metodo_privado()
        return f"Saldo atual: {self.__saldo:.2f}"
    
    def depositar(self, valor: float) -> None:
        self.__saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
    
    def sacar(self, valor: float) -> None:
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado")
        else:
            print("Saldo insuficiente")
    
    def __metodo_privado(self):
        print("Olá, metodo privado")

conta_joao = ContaBancaria("João", 5000)
# print(conta_joao.__saldo)
# conta_joao.titular = "Ricardo"
# conta_joao.__saldo = 2
# print(conta_joao.exibir_saldo())

# conta_joao.depositar(5.25)
# conta_joao.depositar(100)
# conta_joao.sacar(1500)
# conta_joao.sacar(200)
# print(conta_joao.exibir_saldo())

conta_erica = ContaBancaria("Erica", 0)
conta_erica.depositar(4000)
conta_erica.sacar(3500)
print(conta_erica.exibir_saldo())
conta_erica.sacar(5000)
print(conta_erica.exibir_saldo())