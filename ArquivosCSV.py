# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Manipulando arquivos CSV (comma-separeted values)

#Importando o módulo CSV
import CSV

#Gravando um arquivo CSV
with open('arquivos/numeros.csv','w') as arquivo:
  writer = csv.writer(arquivo)
  writer.writerow(('primeira','segunda','terceira'))
  writer.writerow((22,93,55)) 
  writer.writerow ((62,14,76))

#Leitura de arquivos CSV
with open('arquivos/numeros.csv','r') as arquivo:
  leitor = csv.reader(arquivo)
  for x in leitor:
    print('Número de colunas: ',len(x))
    print(x)

#Gerando uma lista com dados do arquivo CSV
with open('arquivos/numeros.csv','r') as arquivo:
  leitor = csv.reader(arquivo)
  dados= list(leitor)#funçaõ list converte o conteudo para uma lista

print(dados)

#Imprimindo a partir da segunda linha
for linha in dados[1:]
  print(linha)

