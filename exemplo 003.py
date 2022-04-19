"""
Exemplo 003: Comandos decisórios e laços
Objetivo: Condicionais
Programadora: Amanda Spitzner
Data: 08/03/2022
Versão: 001
"""

#As notas de um aluno estão armazenadas em uma lista. Calcular a média destas notas.
Lista_notas= [3.4,6.6,8,9,10,9.5,8.8,4.3]
Soma=0
for nota in Lista_notas:
    print(nota)
    Soma= Soma+nota
media = Soma/len (Lista_notas)
print('Media = ', media)