# import modulo_1
import minha_pasta.modulo_2
from modulo_1 import minha_funcao, meu_numero
# import modulo_1 as modulo_renomeado
from datetime import datetime
# import minha_pasta
from minha_pasta import modulo_2, modulo_3


def teste():
    import modulo_1
    modulo_1.minha_funcao()

if __name__ == "__main__":
    modulo_2.minha_funcao()
    modulo_3.minha_funcao()
    print("Olá scprit.py")
    print(meu_numero)
    minha_funcao()
    print(datetime.now())
    print("modulo.py", __name__)
    teste()