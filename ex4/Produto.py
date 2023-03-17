class Produto:
    def __init__(self, codigo, descProduto, preco, quantidade):
        self.codigo = codigo
        self.descProduto = descProduto
        self.preco = preco
        self.quantidade = quantidade

    def calculaPrecoFinal(self):
        precoFinal = self.preco - self.descProduto
        precoQuantidadeTotal = precoFinal * self.quantidade

        return "O produto de código " + self.codigo + " ficou com seu preço final de " + str(precoQuantidadeTotal)