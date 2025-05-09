#Funcoes
# def = function

def saudacao():
    print("Ola seja bem vindo!")
saudacao()

##Funcao com parametros
def saudacao_personalizada(nome):
    print(f"Olá {nome}, seja bem vindo(a)!")
saudacao_personalizada("Tayse Rosa")

##multiplos parametros
def apresentar_pessoa(nome,idade, profissao):
    print(f"Dados da pessoa, nome:{nome}, idade:{idade}, profissão:{profissao}")
apresentar_pessoa("Tayse", 37, "programadora")

##return => Instrução que retorna o valor pro programa
def soma(a, b):
    resultado = a+b
    return resultado
print(soma(5,5))

