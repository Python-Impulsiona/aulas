class Conta:
    def __init__(self, descricao: str, valor: float, ) -> None:
        self.descricao = descricao
        self.valor = valor

class Credito(Conta):
    pass

class Debito(Conta):
    pass

contas = [
    Credito("salario do trabalho", 2000), 
    Debito("conta de luz", 250),
    Debito("conta de internet", 100),
    Credito("dinheiro achado na rua", 100),
]

soma_credito = 0
soma_debito = 0

for conta in contas:
    if conta is Credito:
        soma_credito += conta.valor
    elif conta is Debito:
        soma_debito += conta.valor

print("Soma credito", soma_credito)
print("Soma debito", soma_debito)