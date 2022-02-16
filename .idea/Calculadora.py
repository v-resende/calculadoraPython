print("Bem-vindo a Calculadora")
print("Escolha uma operação: ")
print("1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão")

num1 = 0
num2 = 0

numero = int(input("Digite um número: "))


while (numero >= 5):
    print("Número inválido")
    print("Escolha outro número")
    numero = int(input("Digite um número: "))

if numero == 1:
    print('A operação escolhida foi: Soma!')

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 + num2
    print("O resultado é: ", resultado)

if numero == 2:
    print('A operação escolhida foi: Subtração!')
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 - num2
    print("O resultado é: ", resultado)

if numero == 3:
    print('A operação escolhida foi: Multiplicação!')
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 * num2
    print("O resultado é: ", resultado)

if numero == 4:
        print('A operação escolhida foi: Divisão!')
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2

        print("O resultado é: ", resultado)

















