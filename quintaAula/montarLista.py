# Atividade feita em aula
# Solicita ao usuário uma quantidade de pessoas e, em seguida, permite que o usuário insira os nomes dessas pessoas, armazenando-os em uma lista

quantidade = int(input("Digite a quantidade de pessoas que deseja na lista: "))
contador = 0
pessoas = []

while contador < quantidade:
    pessoa = input("Digite o nome da pessoa: ")
    pessoas.append(pessoa)
    contador += 1

print(pessoas)
