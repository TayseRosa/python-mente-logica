#adivinhe um numero
import random

print("bem vindo ao jogo do 'Adivinhe o número'")

#repetir um codigo ate o usuario aceitar
while True:

    #gerar um numero aleatoria de 1 a 50
    numero_secreto = random.randint(1, 50)
    print(numero_secreto)

    tentativas_restantes = 5

    print("Pensei num numero entre 1 e 50")
    print("Você tem 5 tentativas para adivinhar")

    #loop ate as tentativas acabarem
    white tentativas_restantes > 0:
        #palpite do usuario(input)
        palpite = input("Digite o número:")

        #validação para checar se o usuario digitou um numero
        if not palpite.isdigit():
            print("Entrada invalida!Digite um numero entre 1 e 50")
            continue
        #converter palpute para inteiro
        palpite = int(palpite)
        #ver se o numero esta no intervalo estipulado
        if(palpite < 1 or palpite > 50):
            print("O numero deve ser entre 1 e 50")
            continue

            #descontar tentativas
            tentativas_restantes -=1
        break
    break