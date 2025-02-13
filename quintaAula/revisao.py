"""
Operadores Lógicos

and (True se ambas condições verdadeiras)
or (True se ao menos uma condição for verdadeira)
not (inverte valor lógico)

Operadores Aritméticos
+ adição
- subtração
/ divisão
% modulo
** potencia

Operadores de Comparação
= atribui valor
== igual a (compara igualdades)
!= diferente de
< menor que
< = menor ou igual a
> = maior ou igual a
> maior que

"""

# Revisao if,elif e else
login = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

if login == 'Bia' and senha == '0000' :
    print('Acesso Liberado')
elif login == 'Fulano' and senha == '123':
    print('Acesso Liberado')
else :
    print('Acesso Negado')

# Usando or

cadastro = input('Digite seu nome: ')

if cadastro == 'Ana' or cadastro == 'Julia':
    print("Bem Vindo")
else:
    print("Acesso negado")


#Revisão Lista - estrutura mutável que armazena vários valores ordenados, como um array em javascript

frutas = ["uva", "pera", "maça", "banana"]
print(len(frutas[1])) # Conta quantidade de caracteres da palavra
print(type(frutas))

# Revisão Tupla - é imutável e podde armazenar diferentes tipos de dados

filmes = ("Batman", "Carros", 8, True, "Barbie")
print(filmes)
print(len(filmes)) # Conta quantidade de Itens


# Tupla de números
numeros = (5, 80,31,10,4)
print(max(numeros)) # pega o maior numero da tupla
print(min(numeros))#pega o menor numero da tupla
print(sum(numeros)) #soma todos os numeros da tupla

# Dicionario (dict)

cadastro = {
    'nome': 'mouse',
    'preço': 20,
    'categoria': 'acessório'
}
print(cadastro['nome']) #Acessa e imprime o valor associado a variável

#Loops - while

resposta = input ('Deseja continuar? [S/N]')

while resposta == 'S':
    print('Execute')
    resposta = input ('Deseja continuar? [S/N]')

#Loops - for 
filmes = ("Batman", "Carros", 8, True, "Barbie")
for item in filmes: # percorre cada caracter da lista
    print(item)

#----------------FUNÇÕES-----------

def soma(num1,num2):
    print(num1+num2)

soma(8,2)

#-------------------------------------
def sum(numero1,numero2,numero3):
    return (numero1 + numero2) * numero3

n1 = int(input('Digite uma número: '))
n2 = int(input('Digite uma número: '))
n3 = int(input('Digite uma número: '))

result = sum (n1,n2,n3)

print(result)

