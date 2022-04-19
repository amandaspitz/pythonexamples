"""
Exemplo 006: Comandos decisórios e laços
Objetivo: Condicionais
Programadora: Amanda Spitzner
Data: 08/03/2022
Versão: 001
"""
# Dados de entrada para o volume do cilindro (metros)
raio = float(input('Qual o raio do cilindro em metros: '))
altura = float(input('Qual a altura do cilindro em metros: '))

pi = 3.14 #constante
volume = pi * raio**2 * altura #formula de calculo de volume
print ('\n\nVolume do Cilindro=', volume, 'm3')

litros = volume/3
latas = litros/5

print('Litros=', litros, 'l')
print('Latas necessárias=', latas, 'latas')

#valores
ValorLata = 50.00
ValorTotalLatas = latas * ValorLata

print('\n\nCusto total das latas=', ' R$', ValorTotalLatas)

#Externo do cilindro
AreaLateral= 2* volume
AreaRaio = 2* raio + AreaLateral

print('\n\nÁrea lateral do cilindro= ', AreaLateral, 'm')
print('Área do raio= ', AreaRaio, 'm')



