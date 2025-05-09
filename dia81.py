### Converter Farenheith em Celcius
#Preciso criar a função, aceitar a temperatura em F
#Passar pela formula de conversao (f-32)*5/9
#retornar o valor para o excopo globals
#imprimir o resultado

def farenheith_4_celsius(f):
    return (f - 32) * 5/9

temp_f = 102
temp_c = farenheith_4_celsius(temp_f)

print(f"A temperatura {temp_f}F foi convertida para {temp_c}C")