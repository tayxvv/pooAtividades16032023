class Retangulo:

    def __init__(self, nome, altura, largura):
        self.nome = nome
        self.altura = altura
        self.largura = largura

    def calculaArea(self):
        area = self.altura * self.largura
        area = round(area, 2)
        return "O retângulo " + self.nome + " tem área de " + str(area)