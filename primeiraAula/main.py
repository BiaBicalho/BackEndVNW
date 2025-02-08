# segunda aula back-end, tipos de dados

nome = 'Bia'

nome_azevedo = 'Azevedo'

# Tipos de Dados

# let
temperatura = 30

#float
altura = 1.70
print(type(altura))

#string(str)
frase = "Boa noite!"

#bolean
esta_chovendo = False

#Nulo
resultado = None

#undefined -> cria váriavel sem valor dado
#dia
#print(dia)

# Exibir Soma
primeiro_valor = 5.2
segundo_valor = 1.8
print(primeiro_valor + segundo_valor)

#Exibir frase
tempo = "chuva"
frase = "Não vai dar praia"

print(tempo,frase)

# ------------------
# Input faz o usuario interagir
#nome = input("Qual o seu nome: ")
#print("Olá " + nome)

valor_um = input("Qual o primeiro valor: ")
valor = input("Qual o segundo valor: ")

soma = int(valor_um) + int(valor)

print(f"A soma é: {soma}")