from Produto import Produto

produto1 = Produto("1", 1.0, 3.0, 2)
produto2 = Produto("2", 2.0, 6.0, 4)
produto3 = Produto("3", 3.0, 9.0, 5)

retorno1 = produto1.calculaPrecoFinal()
print(retorno1)

retorno2 = produto2.calculaPrecoFinal()
print(retorno2)

retorno3 = produto3.calculaPrecoFinal()
print(retorno3)