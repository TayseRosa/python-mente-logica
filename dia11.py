#dicionarios - objetos

#array []
#tupla ()
#dicionario {}

aluno = {
    "nome":"Tayse",
    "profissao":"Programadora",
    "idade":37
}

print(aluno['nome'])
print(aluno['idade'])
print(aluno['profissao'])

#adicionar valores
aluno['nota']=100
print(aluno)

#deletar valores
del aluno['profissao']
print(aluno)

#conjunto set
