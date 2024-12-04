class ClasseBase:
    def __init__(self) -> None:
        self.atributo = 0

    def metodo(self):
        print("Metodo da classe base")

class ClasseDerivada(ClasseBase):
    def __init__(self, atributo) -> None:
        super().__init__()
        self.atributo = atributo
    
    def metodo(self):
        print("Metodo da classe derivada")

classe_base1 = ClasseBase()
print(classe_base1.atributo)
classe_base1.metodo()

classe_derivada1 = ClasseDerivada(200)
print(classe_derivada1.atributo)
classe_derivada1.metodo()