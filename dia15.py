#paradigma OO - orientação a objetos
#Classe é um molde do objeto
class Pessoa:
    def __init__(self, nome, idade):
        #colocar o valor do argumento no meu futuro objeto
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        print(f"Olá, meu nome eh {self.nome} e eu tenho {self.idade} anos")

    def aniversario(self):
        self.idade += 1
        print(f"Fiz aniversario, agora eu tenho {self.idade} anos")

pessoa1 = Pessoa("Tayse", 37)
pessoa2 = Pessoa("Theo", 9)
pessoa3 = Pessoa("Pipoka", 12)
pessoa4 = Pessoa("Maria", 99)

#metodo sao as funções do objeto
pessoa1.apresentacao()
pessoa2.apresentacao()
pessoa3.aniversario()
pessoa3.aniversario()
pessoa3.aniversario()
pessoa4.apresentacao()

#Classe retangulo *
#Propriedades = largura, altura *
#Método: para exibir a area

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

ret = Retangulo(10,5)
area_calculada = ret.area()
print(f"O valor da area do retangulo de altura {ret.altura} e largura {ret.largura} é: {area_calculada}")