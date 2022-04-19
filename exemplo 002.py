"""
Exemplo 001: Comandos decisórios e laços
Objetivo: Condicionais
Programadora: Amanda Spitzner
Data: 13/03/2022
Versão: 001
"""
# 0, 1, 2, 3, 5, 8, 13, 21... Sequência Fibonacci # ativa o módulo de funções matemáticas

import math

"""Use a regra de Fibonacci (cada elemento soma com o anterior) para gerar uma sequência de N números Fibonacci ou
de números positivos ou negativos (um dos dois iniciais deve ser diferente de zero e a razão entre cada dois elementos consecutivos;
estes ultrapassarem 999 haverá perda do alinhamento dos resultados"""

print('Deseja a sequência de Fibonacci (F) ou uma qualquer (Q)?')
resposta='X'
# Verifica se a resposta foi F ou Q, senão insiste
while Resposta =! 'F' and Resposta =! 'Q':
    Resposta=input('Digite F ou Q: ')
    if Resposta == 'F':
        FibA = 1
        FibB = 1
    elif Resposta == 'Q':
        while True:
            FibA = int(input('Entre com o primeiro número: '))
            FibB = int(input('Entre com o segundo número: '))
            if FibA == 0 and Fib ==0
                print('Um deles deve ser diferente de 0 ')
            else: break #break faz ele sair do while
while True:
    Ult=int(input('Entre com o número de elementos: '))
    if Ult <=1:
        print('O número de elementos deve ser >= 2!')
    else: break
#imprime os títulos da tabela
if Resposta == 'F':
    print(' N Fib(N) Razão')
else:
    print(' N Qqer(N) Razão')
#imprime os dois primeiros elementos
    if Resposta == 'F'
        print('001 001')
        print('002 001 1.0')
    else: # Resposta foi Q
        if FiBA>=0:

            #não terminado
