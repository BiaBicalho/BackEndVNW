
from xml.sax.saxutils import prepare_input_source


lista_compra = ['laranja', 'leite', 'ovos', 'macarrão']

print(lista_compra) # mostra todos is itens 

print(lista_compra[0]) # chama o 1ºitem
print(lista_compra[0:2]) #conta 2 itens
print(lista_compra[-1]) #imprime o 1º de trás pra frente

#------------------Insert---------------------------------
frutas = ["maça","uva","pera","pessego", "maça"]
frutas.insert(2,"banana")
print(frutas)

#------------Append-------

frutas.append('abacaxi') #adiciona o item no final da lista
print(frutas)

#---------------sort-------
frutas.sort() #ordena por rdem numerica ou alfabetica
print(frutas)

numeros = [3,20,10,18,2,57,14]
numeros.sort()
print(numeros)

#-----------Remove----

#frutas.remove("maça") #remove o item especificado, com o nome
print(frutas)


#========pop-----

frutas.pop() #remove o ulyimo item da lista
frutas.pop(1) # remove o item pelo index especificado
print(frutas)

#-----------count------------

quantidade = frutas.count("maça")
#cria uma copuia da lista e armazena ela em algum lugar
print("quantidade: ",quantidade)

#TUPLAS

first_tupla = ("mali",72, True, "banana")
second_tupla = 34, "ana", "maça", 17420, False
print(second_tupla)

dados = ["nome", 'senha', ('rg', 'cpf'), 'idade', True] #lista com uma tupla dentro

# dá pra concatenar duas tuplas

pratos= ("Arroz", "Feijão")
pratos2=("Lasanha", "Yakissoba")

novos_pratos = pratos + pratos2

print(novos_pratos)

print("feijoada" in novos_pratos)

#-------kista para tupla----

lista = [1,5,7]

tuple = tuple(lista)

print(type(tuple))

print(tuple)

# --------tupla para lista

nova_lista = list(tuple)
print(type(nova_lista))

print(nova_lista)