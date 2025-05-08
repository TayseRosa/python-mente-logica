#estrutura de repetição
frutas = ["maçã", "banana", "laranja"]
###
for f in frutas:
        print('Fruta: ',f)

###
for i in range(5):
        print ("Number: ", i)        
###
print(frutas[2])
###
count = 0
while count < 5:
        print("Num while: ", count)
        count += 1
###
for i in range(10):
        if i == 5:
                break        
        print("Num for", i)
###
for i in range(10):
        if i == 2:
                continue
        print("For i in continue", i)

##calcular a multiplicação de 1 a n
N = int(input("Digite um numero"))
multiplicação = 0

for i in range(1, N+1):
        resultado = N * i
        print(resultado)
###Identificar numeros pares e impares ate 20
pares = 0
impares = 0

for i in range(1, 6):
        if i % 2 == 0:
                pares +=1
        else:
                impares +=1
        print("Pares: ", pares)
        print("Impares: ", impares)