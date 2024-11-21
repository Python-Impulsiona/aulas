try:
    #...
    print(0/0)
except ZeroDivisionError:
    print("Não é possível dividir por zero")

lista = [1,2,3]

try:
    print(lista["d"])
except IndexError:
    print("Index inválido")
except Exception:
    print("Não pode ser texto, exceção genérica")


try:
    with open("teste.txt", "r") as arquivo:
        print("Arquivo aberto!!")
except FileNotFoundError:
    print("Arquivo não encontrado")


# try:
#     # consumir api/backend
# except Exception:
#     print("Sistema x indisponivel")