mensagem = "Olá mundo"
print(mensagem)

def encontrar_maior(numeros = []):
  if len(numeros) == 0:
    print("Lista vazia")
  else:
    maior = numeros[0]
    for numero in numeros:
      if numero > maior:
        maior = numero
    print(f"O número maior é {maior}")

# encontrar_maior([100,2,6,99])
# encontrar_maior([-5,-55,-2])
# encontrar_maior()

print("__name__", __name__)

if __name__ == "__main__":
  encontrar_maior([100,2,6,99])