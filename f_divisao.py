from f_verifica_number import verificar_number1
def divisao():
    num1 = input("Digite o primeiro número: ")
    verificar_number1(num1)
    op1 = verificar_number1(num1)
    num2 = input("Digite o segundo número: ")
    verificar_number1(num2)
    op2 = verificar_number1(num2)
    if(op1 == 0 or op2 ==0):
        print('Não faça divisão por zero,Retorne para a divisão!!')
        return divisao()

    div = op1/op2
    print('A divisão é é: ',div)
    