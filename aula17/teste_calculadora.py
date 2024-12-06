import unittest
import calculadora

class TesteCalculadora(unittest.TestCase):
    def testar_soma(self):
        resultado_positivo = calculadora.somar(3,4)
        resultado_negativo = calculadora.somar(2,-4)
        resultado_zerado = calculadora.somar(0,0)

        self.assertEqual(
            resultado_positivo, 
            7, 
            "Erro na soma de valores com resultadopositivo"
        )
        self.assertEqual(resultado_negativo, -2, "Erro na soma de valores para resultado negativo")
        self.assertEqual(resultado_zerado, 0, "Erro na soma de valores para resultado zerado")

    def testar_subtracao(self):
        resultado = calculadora.subtrair(5,3)
        self.assertEqual(resultado, 2, "Erro na subtração")
    
    def testar_multiplicacao(self):
        resultado = calculadora.multiplicacao(5,3)
        self.assertEqual(resultado, 15, "Erro na multiplicação")
    
    def testar_divisao(self):
        resultado = calculadora.divisao(6,3)
        resultado1 = calculadora.divisao(0,3)
        resultado2 = calculadora.divisao(3,0)
        self.assertEqual(resultado, 2, "Erro na divisao")
        self.assertEqual(resultado1, "Operação inválida", "Erro na divisao")
        self.assertEqual(resultado2, "Operação inválida", "Erro na divisao")

if __name__ == "__main__":
    unittest.main()