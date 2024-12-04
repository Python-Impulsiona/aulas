class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario = salario_base
    
    def calcular_salario(self):
        return self.salario

class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario + 2000

class Vendedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, valor_total_vendas: float) -> None:
        super().__init__(nome, salario_base)
        self.valor_total_vendas = valor_total_vendas

    def calcular_salario(self):
        comissao = self.valor_total_vendas * 0.05
        return self.salario + comissao

class Desenvolvedor(Funcionario):
    pass

diego = Gerente("Diego", 10000)
print(diego.nome, diego.calcular_salario())

angela = Vendedor(nome="Angela", salario_base=5000, valor_total_vendas=2500)
print(angela.nome, angela.calcular_salario())

alan = Desenvolvedor("Alan", 15000)
print(alan.nome, alan.calcular_salario())