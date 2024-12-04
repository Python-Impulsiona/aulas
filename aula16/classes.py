# Orientação a objetos

# modelos representam objetos

class MinhaClasse:
    atributo_padrao = None

    def __init__(self, meu_valor):#construtor da classe
        self.atributo = meu_valor
    
    def fazer_alguma_coisa(self):
        print(f"Olá, o valor do atributo é {self.atributo}")

minhaClasse1 = MinhaClasse("meu valor")
# print(minhaClasse1)
# print(minhaClasse1.atributo)
# minhaClasse1.fazer_alguma_coisa()

minha_classe2 = MinhaClasse(123)
# minha_classe2.fazer_alguma_coisa()
# print(minhaClasse1.atributo_padrao)
# print(minha_classe2.atributo_padrao)

class Aluno:
    nome = None

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

turma_python: list[Aluno] = [
    Aluno("Fred", 30),
    Aluno("Alan", 30),
    Aluno("Luis", 30),
    Aluno("Flavio", 30)
]

# for aluno in turma_python:
#     aluno.apresentar()

class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def vender(self, quantidade: int):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"Venda realizada: {quantidade} unidades")
        else:
            print("Estoque insuficiente.")
    
    def exibir_estoque(self) -> str:
        return f"Estoque atual de {self.nome}: {self.estoque} unidades."
    
computador = Produto("Computador Gamer", 3000, 5)
celular = Produto("Xiaomi", 1400, 3)

computador.vender(4)
print(computador.exibir_estoque())
computador.vender(1)
print(computador.exibir_estoque())
computador.vender(2)

celular.vender(2)
print(celular.exibir_estoque())
celular.vender(1)
print(celular.exibir_estoque())
celular.vender(2)
