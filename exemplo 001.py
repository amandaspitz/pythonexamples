"""
Exemplo 001: Comandos decisórios e laços
Objetivo: Condicionais
Programadora: Amanda Spitzner
Data: 13/03/2022
Versão: 001

"""


# primeiro criar uma funcao por ex. função de checar o CPF, dai posso usar em vários programas, em vários códigos. Aqui defini a função calcula

def calcula(a, b, c):
    adicao = a + b + c
    return adicao


# função é similar a uma calculadora, vc define ela e ela devolve o resultado
resultado = calcula(9, 5, 10)
print(resultado)

resultado = calcula(9, 5, 10) / 3
print(resultado)

# ???posso declarar o mesmo nome duas vezes? 'resultado'???