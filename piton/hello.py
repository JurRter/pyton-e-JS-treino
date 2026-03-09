def soma(a, b):
    return a + b

def printstring():
    string = input("Digite uma string: ")
    print(f"Você digitou: {string}")
    return string

def data():
    dia = input("Que dia você nasceu")
    mes = input("Qual mes você nasceu")
    ano = input("Qual ano você")
    print(f"{dia}/{mes}/{ano}")
    
def tchurusbangos():
    nome = input("Qual teu nome ze ")
    idade = input("Qual tua idade ")
    peso = input("Qual teu peso ")

    print(f"seu nome é {nome}\nsua idade: {idade}\nseu peso: {peso}")

def calculadora():
    
    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Raiz")
        print("7. Sair")
        escolha = input("Digite o número da operação desejada: ")
        if escolha == '7':
            print("Encerrando a calculadora.")
            break
        num1 = float(input("Digite o primeiro número: "))
        if escolha in ['5']:
            num2 = float(input("Digite o expoente: "))
        elif escolha in ['6']:
            num2 = float(input("Digite o índice da raiz: "))
        else:
            num2 = float(input("Digite o segundo número: "))

        

        if escolha == '1':
            resultado = num1 + num2
            print(f"O resultado da soma é: {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif escolha == '5':
            resultado = num1 ** num2
            print(f"O resultado da potenciação é: {resultado}")
        elif escolha == '6':
            if num1 >= 0:
                resultado = num1 ** (1/num2)
                print(f"O resultado da raiz é: {resultado}")
            else:
                print("Erro: Não é possível calcular a raiz de um número negativo.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    data()
    calculadora()
