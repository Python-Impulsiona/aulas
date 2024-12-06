def somar(a: int | float, b: int | float) -> int | float:
    return a + b

def subtrair(a: int | float, b: int | float) -> int | float:
    return a - b

def multiplicacao(a: int | float, b: int | float) -> int | float:
    return a * b

def divisao(a: int | float, b: int | float) -> int | float | str:
    if a == 0 or b == 0: return "Operação inválida"
    return a / b