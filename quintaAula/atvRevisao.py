"""
texto = 'python é uma linguagem poderosa é fácil de aprender'
quant_caracteres = len(texto)
print("o texto contém", quant_caracteres,"caracteres")

a = [1,2,3]
b = a
b.append(4)
print(b)

#Contagem regressiva a partir de um número
def contagem_regressiva(n):
    while n >= 0:
        print(n)
        n -= 1

contagem_regressiva(8)

#
nota1 = float(input("Digite a 1ºnota: "))
nota2 = float(input("Digite a 2ºnota: "))
nota3 = float(input("Digite a 3ºnota: "))

media = (nota1 + nota2 + nota3) / 3
print("A média do aluno é :", media)

#
numeros = [10, 25, 5, 8, 30, 20]

maior = max(numeros)
numeros.remove(maior)

segundo_maior = max(numeros)
print("O segundo maior número é: ", segundo_maior)

# Simular Calculadora
from itertools import product
import numbers
from tkinter import N


num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+ , - , * , /): ")
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação Inválida"
print ("Resultado: ", resultado)
"""

numeros = [1, 2, 3, 4, 6, 7, 8]
produto = 1

for n in numeros:  # Apenas números, excluindo booleanos
    produto *= n  # Multiplica os valores válidos

print("O produto dos números é:", produto)
"""
numeros = [None, 1, 2, True, 3, 4, False, 6, 7, 8]
produto = 1

for n in numeros:
    if isinstance(n, (int, float)) and not isinstance(n, bool):  # Apenas números, excluindo booleanos
        produto *= n  # Multiplica os valores válidos

print("O produto dos números é:", produto)
"""