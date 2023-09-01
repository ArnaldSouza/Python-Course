# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:00:50 2021

@author: Arninho
"""

import aula_03_mod
import path
import numpy as np
import matplotlib.pyplot as plt

x = np.sin(np.linspace(0, 5*np.pi, 100))
plt.plot(x)

# ativa seções do código
REVISAO = False
DATA_STR = False
MODULOS = False
CLASSES = False
HELP_DIR = False

# revisão:
def revisao(msg):
    """ Revisão """    
    
    msg = "teste"
    
    # strings e listas
    print('*' * 30 , '\n', msg)
    pares = [0, 2, 4, 6]
    print("lista pares: ", pares)
    print("terceiro elemento em diante: ", pares[2:])
    pares  = pares + [8, 10]
    print("lista após aumento: ", pares, "\n")

    # condicionais
    if len(pares) < 3:
        print('que lista curta!')
    else:
        print('até que tem bastante coisa ae...')

    # laço de repetição
    print('\n quadrados:')
    for n in pares:
        print("%d: %d," % (n, n**2), end=' ')        

    return "\n\nfeitoria, terminou a revisão"

def tuplas():
    """" demonstarção de tuplas """
    
    print('-' * 30, "\ntuplas")

    # definindo uma tupla e desempacotando
    tup = ("zé", 22, 67.9)
    nome, idade, peso = tup
    
    # teste de uso
    print(tup)
    print('Seu %s tem %d anos e pesa %.2f Kg.' % (nome, idade, peso))
    print('Seu %s tem %d anos e pesa %.2f Kg.' % tup)
    print('\n')


def dicionarios():
    """" demonstarção de dicionários """
    
    print('=' * 30, "\n"+"dicionários"+"\n")
    
    # definindo dicionários
    sensores = {"temp_sala": 22.1, "temp_rua": 17.9, "luz_sala": "ligado"}
    print("->dic: ", sensores)
    print("temperatura da sala: ", sensores['temp_sala'])

    # adicionando itens
    sensores['luz_rua'] = 'desligado'
    
    # iterando (percorrendo)
    print("\n->itens do dicionário", '\n')
    for k, v in sensores.items():
        print(k, v)
    
# módulos
def modulos():
    x = aula_03_mod.quadrado(4)
    print(x)

# list comprehension
def list_comp():
    list_1 = [i for i in range(10)]
    list_2 = [i for i in range(10) if i%2 == 0]
    list_3 = [a + 5 for a in list_1]
    
    print("L1: ", list_1)
    print("L2: ", list_2)
    print("L3: ", list_3)
    

# classes
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresenta(self):
      print("Eae gentalha, me chamo %s e tenho %d anos" % (self.nome, 
                                                           self.idade))

# função main - testa se cada seção está ativa
if __name__ == "__main__":
    if REVISAO:
        res = revisao("começando a revisão:")
        print(res)
    if DATA_STR:
        tuplas()
        dicionarios()
    
    if MODULOS:
        modulos()
        
    if CLASSES:
        P1 = Pessoa('Fabio', 40)
        dir(P1)
        P1.nome
        P1.apresenta()
        P1.idade = 75
        P1.apresenta()

    if HELP_DIR:
        frase = 'conversa entre dois tobogãs: Nossa, como os anus passam depressa.'
        dir(frase)        
        help(frase.capitalize)
        frase.capitalize()
        frase.title()
        x = frase.split()
        x.sort()
        frase.sort()

        teste_dic = {}
        print(dir(teste_dic))
        print(help(teste_dic.keys))


# problemas: 2591, 1255, 1273

#https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

# 1) ignorar case ('função lower')
# 2) criar dicionário onde as chaves são os caracteres, e valores as
# quantidades de caracteres
# 3) encontrar frequencia maxima
# 4) adicionar os caracteres mais frequentes em uma lista   
# 5colocar lista em ordem crescente função sort
# 6)imprimir os caracteres depois de ordenados

