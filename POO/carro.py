# A palavra "class" e usada para criar uma classe.
# Uma classe e como um molde para criar objetos
class carro:
    # "def" definir uma função ou método
    # "_init_" e o método construtor da classe
    # eEe e execultado automaticamente quando um objeto é criado
    # "self" representa o proprio objeto
    # É através do self que apresentamos atributos e metodos do objeto
    # "marca", "modelo", "ano" e "velocidade"
    # São parametros recebidos pela classe.
    def _init_(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

        #criando um objeto da classe carro

        # "carro1" e uma váriavel que recebe um objeto

        carro1 = carro("chevrolet", "S10", 2013)
        #exibir informações do carro
        print(f"Marca: {self.marca}")