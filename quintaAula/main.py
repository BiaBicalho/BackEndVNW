"""
Operadores Lógicos

and &&
or ||
not ##

Operadores Aritméticos
+ adição
- subtração
/ divisão
% modulo
** potencia

Operadores de Comparação
== igual a
!= diferente de
< menor que
< = menor ou igual a
> = maior ou igual a
> maior que

"""
cadastro = input('Digite sua senha: ')

if cadastro == '1234' or cadastro == '0000' :
    print('Acesso Liberado')
else :
    print('Senha incorreta')

#Revisão Lista

frutas = ["uva", "pera", "maça", "banana"]
print(len(frutas[1])) # Conta quantidade de caracteres da palavra
print(type(frutas))

# Revisão Tupla 

filmes = ("Batman", "Carros","Frozen", "Barbie")
print(filmes)
print(len(filmes)) # Conta quantidade de Itens

numeros = (5, 80,31,10,4)
print(max(numeros)) # pega o maior numero da tupla
print(min(numeros))#pega o menor numero da tupla
print(sum(numeros)) #soma todos os numeros da tupla