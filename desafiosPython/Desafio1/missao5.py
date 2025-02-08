""" Missão 5: Recuperando o Cofre de Segurança 🔒

O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! 
Agora, apenas quem souber a combinação correta poderá acessá-lo.
Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".
"""

senha = "" 

while senha != "Python123":
    senha = input("Digite a senha: ")
    if senha == "Python123":
        print("Senha Correta. Acesso Liberado")
    else:
        print("Senha Incorreta. Acesso Negado")

print("Aproveite o Acesso")