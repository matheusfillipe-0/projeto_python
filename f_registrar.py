import getpass
from f_login import usuarios
from f_verifica_number import verificar_number1
from f_verifica_string import verificao_string
from f_valida_endereco import valida_endereco




def registrar():
    novo_login = input("Crie seu nome de usuário: ")
    verificao_string(novo_login)
    nova_senha = getpass.getpass("Crie sua senha: ")
    verificar_number1(nova_senha)
    novo_endereco = input("Digite seu endereço: ")
    valida_endereco(novo_endereco)
    novo_telefone = input("Digite seu telefone: ")
    verificar_number1(novo_telefone)
    novo_usuario = {
        "login": novo_login,
        "senha": nova_senha,
        "endereco": novo_endereco,
        "telefone" :novo_telefone
        
    }
    usuarios.append(novo_usuario)
    print("Parabéns, sua conta foi criada com sucesso!")