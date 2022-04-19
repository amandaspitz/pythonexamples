"""
Exemplo 004: Fixação
Objetivo: 2. Rad (-2 * C) div 4 substituindo ficaria #(-2*-8)//4
Programadora: Amanda Spitzner
Data: 05/03/2022
Versão: 001
"""

import math

#opção 1:
print((-2*-8)**(1/2)//4)

#opção 2:
raiz = (-2*-8) # preciso armazenar parte numa variação para ser passada como parâmetro para a função math.sqrt
math.sqrt(raiz)//4
