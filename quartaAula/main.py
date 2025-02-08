#--------- DICIONARIO E FUNÇÕES --------------------
# dicionario é parecido com objeto do javascript

alunos = {
    'nome' : "ana",
    'idade' : 21,
    'altura':1.70
}

alunos['cidade'] = 'são paulo'
alunos['nome'] = 'bia'
#----------------------------------
alunos.update({'cpf':5158418714, 'aluno': True}) # atualiza com novos dados no dicionário

# delete - deleta a chave e o valor associado
del alunos['altura']

ultimo_numero = alunos.popitem() # pega o ultimo item e guarda em uma variável
print(ultimo_numero)

alunos.clear() # excluir todos os dados do dicionário, também funciona com lista

print(alunos)
