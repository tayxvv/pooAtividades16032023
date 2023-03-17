from Pessoa import Pessoa

pessoa1 = Pessoa("Tayssa", 1.60, 56.4)
pessoa2 = Pessoa("Victoria", 1.63, 56.7)
pessoa3 = Pessoa("Oliveira", 1.70, 53.5)

imcRetorno1 = pessoa1.calculaImc()
print(imcRetorno1)

imcRetorno2 = pessoa2.calculaImc()
print(imcRetorno2)

imcRetorno3 = pessoa3.calculaImc()
print(imcRetorno3)