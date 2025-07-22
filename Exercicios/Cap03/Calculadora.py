# Funções para as operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

# Função para mostrar o menu
def mostrar_menu():
    print("\n=== CALCULADORA SIMPLES ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

# Programa principal
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1 a 5): ")

    if escolha == "5":
        print("Encerrando a calculadora. Até logo!")
        break

    if escolha not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    # Entradas dos números (sem tratamento de erro)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == "1":
        resultado = somar(num1, num2)
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif escolha == "2":
        resultado = subtrair(num1, num2)
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif escolha == "3":
        resultado = multiplicar(num1, num2)
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif escolha == "4":
        resultado = dividir(num1, num2)
        print(f"Resultado: {num1} / {num2} = {resultado}")
