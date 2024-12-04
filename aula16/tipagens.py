#tipos básico
texto: str = ""
inteiro: int = 5
decimal: float = 5.5
booleano: bool = True

#tipos de coleção
numeros: list = [1,2,3]
tupla: tuple = (1,2,3)
conjunto: set = {1,2,3}
dicionario: dict = {"chave1": "valor1"}

numeros_decimais: list[float] = [1.5, 6.2]
tupla_numeros_inteiros: tuple[int, int ,str] = (1,2, "3")
conjunto_numeros_inteiros: set[int] = {2,3}
dicionario_inteiros: dict[str, int] = {"chave2": 2}

def somar(a: int, b: int) -> int :
    return a + b

print(somar(3, 4))

def saudacao(nome: str = "Fulano") -> str:
    return f"Olá, {nome}"

print(saudacao("Pedro"))