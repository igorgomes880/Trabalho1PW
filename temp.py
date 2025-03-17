while True:
    numero = input("Digite um número inteiro: ")
    try:
        numero_int = int(numero)
        break
    except ValueError:
        print("você não digitou um valor inteiro. Tente novamente.")
posterior = numero_int + 1
print(f"O posterior é {posterior}.")