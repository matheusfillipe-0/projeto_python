from f_verifica_number import verificar_number1


def adicao():
    num1 = input("Digite o primeiro número: ")
    op1 = verificar_number1(num1)
    num2 = input("Digite o segundo número: ")
    op2 = verificar_number1(num2)
    soma = op1+op2
    print('A soma é: ',soma)