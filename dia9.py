#Strings
mensagem ="This is a text"
print(mensagem)

#concatenação
name = "Tayse"
lastName = "Rosa"
print(name,lastName)

#repetir strings
decoracaoTitulo = '-'*10
print(decoracaoTitulo + "MENU" + decoracaoTitulo)

repete = "repete isso | " * 10
print(repete)

#Indexação
texto = "Python"
print(texto[3])

#Slice - fatiamento reparte parte do texto
frase = "Aprender Python é bem legal"
print(frase[9:])

#Comprimento de string - lenght
print(len(frase))

texto = "programação é muito legal!"
print(texto.upper())#maiuscula
print(texto.lower())#minuscula
print(texto.title())#Alternando As Palavras

#limpeza de espaço em brancos
msg_com_espaco="       quero falar com o suporte"
print(msg_com_espaco)
print(msg_com_espaco.strip())

#substituicao
frase = "eu gosto de Java"
print(frase)
print("*** Mudou para ***")
nova_frase = frase.replace("Java", "Python")
print(nova_frase)

#Encontrando parte de um texto
texto = "onde esta minha chave?"
posicao = texto.find("chave")
print(f"A posição é {posicao}")

posicao2 = texto.find("key")
print(f"A posição é {posicao2}")
if posicao2 == -1:
    print("Palavra não encontrada")