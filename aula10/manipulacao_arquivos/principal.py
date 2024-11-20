from datetime import datetime 
def ler_arquivo():
    arquivo = open("aula10/manipulacao_arquivos/exemplo.txt", "r")

    # print(arquivo.buffer)
    # print(arquivo.name)
    # print(arquivo.readline())
    # print(arquivo.readlines())

    for linha in arquivo.readlines():
        print(linha)

    arquivo.close()

def escrever_arquivo():
    data_atual = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    with open("aula10/manipulacao_arquivos/minha_pasta/exemplo2.txt", "a", encoding="UTF-8") as arquivo:
        # arquivo.write("\nConteúdo inserido através do código")
        arquivo.write(data_atual)
        arquivo.writelines([
            "\nLinha 1 inserida", 
            "\nLinha 2 inserida", 
            "\nLinha 3 inserida\n"
        ])

        
    print("Arquivo exemplo2.txt alterado")

escrever_arquivo()