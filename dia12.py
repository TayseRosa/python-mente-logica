#tratamento de erros e excessoes
try:
    arquivo=open('dado.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
        print("Erro, o arquivo nao existe!")
else:
    print("Arquivo lido!")
    print(conteudo)
finally:
    print("Operação finalizada")