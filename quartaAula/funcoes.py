# -------- FUNÇÕES --------

# def nomeDaFunção(parametro):

def minha_funcao():
    print("Olá seja bem vindo!!")

minha_funcao() # A chamada de função deve respeitar a indentação para funcionar

# ---------------------------------

def criar_email():
    """
    Solicita o nome e o domínio ao usuário e cria um endereço de email.
    
    Retorna:
     O endereço de email completo.
    """
    nome = input('Digite o nome: ')
    dominio = input('Digite o domínio: ')
    endereco_email = f'{nome}@{dominio}.com'
    return endereco_email

# Exemplo de uso
print(criar_email())


def somar (*args):
    result = 0
    for num in args:
        result +=num
    return result
print(somar(1,5,7,9))
