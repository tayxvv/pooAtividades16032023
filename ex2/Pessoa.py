class Pessoa:

    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def calculaImc(self):
        imc = self.peso / (self.altura * self.altura)
        imc = round(imc, 2)
        return "A pessoa " + self.nome + " tem imc de " + str(imc)