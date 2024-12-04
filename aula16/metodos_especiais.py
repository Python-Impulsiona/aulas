class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco
    
    def __eq__(self, outro: object) -> bool:
        return self.nome == outro.nome
    # less than
    def __lt__(self, outro: object) -> bool:
        return self.preco < outro.preco
    


produto1 = Produto("Camiseta", 50)
produto2 = Produto("Calça", 80)
produto3 = Produto("Camiseta", 40)

# print(produto1 == produto3)
# print(produto1 == produto2)
# print(produto2 > produto1)
# print(produto3 < produto1)


class ContaBancaria():
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self.saldo = saldo
    
    def __add__(self, outro):
        return self.saldo + outro.saldo
    
    def __sub__(self, outro):
        return self.saldo - outro.saldo
    
    def __str__(self) -> str:
        return f"titular: {self.titular} saldo: {self.saldo}"

conta1 = ContaBancaria("João", 1500)
conta2 = ContaBancaria("Maria", 2000)
print(conta1 + conta2)
print(conta1 - conta2)
print(str(conta1))