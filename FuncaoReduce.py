# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Funções Built-in para Data Science

#Função Reduce
#Ela é uma função de recebe 2 argumentos: uma função e uma sequência 'lista'
# reduce(função,sequencia) 
#Ela é aplicada até que haja apenas um elemento da sequencia

#Importando a função reduce do modulo functools
from functools import reduce

#Criando uma lista
lista =[49,25,16,43]

#Função
def soma(a,b):
  x = a + b
  return x

#Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
reduce(soma,lista)

from IPython.display import Image
Image('arquivo/reduce.png')

#Criando uma lista
lst = [56,32,14,58]

#Usando a função reduce() com lambda
reduce ( lambda x,y: x+y, lst)

#Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b
type (max_find2)

#Reduzindo a lista até o valor máximo, atraves da funcao criada com a expressao lambda
reduce(max_find2, lst)#Retorna o maior elemento '58'