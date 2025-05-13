#Trabalhar com arquivos em Python

#Uma forma de ler o arquivo todo
with open('dado.txt', 'r')as arquivo:   #r = leitura /read
    conteudo = arquivo.read()
    print(conteudo)


#ler o arquivo linha por linha
with open('dado.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip()) 
        break

#Criar e escrever em um arquivo(sobreescreve o conteudo)
#a - Append - Adicionar
#r - Read - Ler
#w - Write - Escrever/substituir
with open('saida.txt', 'w') as arquivo:
    arquivo.write('nova linha \n')
    arquivo.write('nova linha2 \n')

#Tipo de arquivo CSV(Excel) - 
import csv
with open("contatos.csv", "w", newline='') as arquivo_csv:
    #Colunas / cabeçalhos
    #dados
    #dados
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Profissão', 'Idade'])
    escritor.writerow(['Tayse', 'Programadora', '37'])
    escritor.writerow(['Joao', 'Profissão B', 'Idade'])
    escritor.writerow(['Maria', 'Profissão C', 'Idade'])
    
#Json
import json
dados = {
    'nome':'Tayse',
    'idade':37,
    'profissao':'programadora'
}
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
