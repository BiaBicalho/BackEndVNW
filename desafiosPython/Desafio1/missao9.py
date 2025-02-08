""" Missão 9: Calculando Dobro de um Número 🛠️

Os alunos precisam de um programa que ajude em cálculos rápidos. 
Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
➡️ Exemplo: dobro(5)
➡️ Saída: "O dobro de 5 é 10"
"""

# Sem Loop
"""
num = int(input("Digite um número: "))

dobro = num * 2

print(f"O dobro de {num} é {dobro}")
"""

#Com Loop
num = ''

while num != 0:
    num = int(input("Digite um número (ou 0, para sair do programa) : "))
    dobro = num * 2
    print(f"O dobro de {num} é {dobro}")
print("Saindo ........")