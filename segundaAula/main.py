# Aula Condicional

saldo = True

if saldo == True: 
    print("Saldo na Conta")
else:
    print("Saldo Indisponível")

#---------------------------------

idade = 16

if idade >= 18:
    print('Pode tirar habilitação')
else:
    print('Não pode tirar habilitação')

#-----------------------------------------

idade = 18
saldo = True

if idade >= 18 and saldo == True:
    print("Pode tirar habilitação")
elif idade < 18 and saldo == False:
    print("Você não tem dinheiro e nem idade para tirar habilitação")
else:
    print("Condição não foi atendida")

#------------------------------------------------------------------------

idade = 18
saldo = True

if idade >= 18 and saldo == True:
    print("Pode tirar habilitação")
elif idade < 18 or saldo == False:
    print("Você não tem dinheiro ou não tem idade para tirar habilitação")
else:
    print("")

#-------------------------------------------
cor = "Alguma cor"

if cor == 'verde':
    print("Acelerar")
elif cor == "amarelo":
    print("atenção")
else:
    print('parar')
#--------------------------------

for caractere in 'Python': #percorre a palavra
    print(caractere)

#-------------------------------------

lista_sonhos = ["Tailândia", "Suiça", "México", "Dinamarca"]

for item in lista_sonhos:  
    #percorre indice do array
    print(item)

# ___While_________

contador = 0
while contador <=10:
	print (contador)
	contador += 1

#------Métodos em Python-------------

# .upper() deixa tudo maiúsculo

lanche = "Pizza"
#print(lanche.upper()) 
print ('Seu lanche é:{lanche}')