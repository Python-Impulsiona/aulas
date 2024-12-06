from unittest import TestCase, main
from unittest.mock import patch

#Mock = mudar o comportamento de métodos/funções 
def perguntar():
    nome = input("Qual é o seu nome? ")
    idade = input("Qual é a sua idade? ")
    return f"{nome} tem {idade} anos"

class TestePergunta(TestCase):

    @patch("builtins.input")
    def testar_pergunta(self, mock_input):
        # simula multiplas entrada para o método input
        mock_input.side_effect = ["Fulano", "30"]

        retorno = perguntar()
        self.assertEqual(retorno, "Fulano tem 30 anos", "Erro na função perguntar()")
        self.assertEqual(mock_input.call_count, 2, "A função input não é chamada 2 vezes")
        
        mock_input.assert_any_call("Qual é o seu nome? ")
        mock_input.assert_any_call("Qual é a sua idade? ")

        mock_input.side_effect = ["Cicrano", "23"]
        retorno2 = perguntar()
        self.assertEqual(retorno2, "Cicrano tem 23 anos", "Erro na função perguntar()")

if __name__ == "__main__":
    main()