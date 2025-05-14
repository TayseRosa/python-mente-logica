#Padrão de Projeto
#Singleton = garantir que uma classe tenha apenas 1 instância
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Instãncia Singleton criada")
        return cls._instance

    obj1 = Singleton()