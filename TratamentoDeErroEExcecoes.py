# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Tratamento de exceções
#Try,Except,Finally

#Utilizando Try e except
try:
  8 +'s'
except TypeError: #Erro de sintaxe, por exemplo
  print('Operação não permitida!')

#Utilizando Try, except e else
try:
  f = open('arquivo/testandoerros.txt','w')
  f.write("Gravando no arquivo")
except IOError: #Erro de entrada ou saida
  print('Erro: arquivo não encontrado ou não pode ser gravado.')
else:
  print("Conteudo gravado com sucesso!")
  f.close()

#Utilizando Try, except, else e finally
try:
  f = open('arquivo/testandoerros.txt','w')
  f.write("Gravando no arquivo")
except IOError: #Erro de entrada ou saida
  print('Erro: arquivo não encontrado ou não pode ser gravado.')
else:
  print("Conteudo gravado com sucesso!")
  f.close()
finally:
  print('Comandos no bloco finally são sempre executados!')

#Usando askint() 
def askint():
  try:
    val = int((input('Digite um numero: ')))
  except UnboundLocalError:
    print('Você não digitou um numero.')
  finally:
    print('Obrigado!')
  print(val)
  
askint()

def askint():
  while True:
    try:
       val = int((input('Digite um numero: ')))
    except:
       print('Você não digitou um numero.')
       continue#Obriga o usuario a digitar um numero
    else:
      print('Obrigado por digitar um numero.')
      break
    finally:
       print('Obrigado!')
    print(val)

askint()

#Capturando o codio de erro.
tuple = (1,2,3,4,5)
try:
  tuple.apped(6)
  for each in tuple:
    print(each)
except AttributeError as e:
  print("Erro: ",e)
except IOError as e:
  print('Erro de I/O: ',e)