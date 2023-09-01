# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:19:28 2021

@author: Arninho
"""

#Neste problema estamos interessados na frequência das letras em uma dada linha de texto.

#Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência do texto, ignorando
# o “case sensitive”, ou seja maiúsculas ou minúsculas (sendo mais claro, “letras” referem-se precisamente
#às 26 letras do alfabeto).
#Entrada
#A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de
# casos de teste. Cada caso de teste consiste de uma única linha de texto. A linha pode conter caracteres 
# “não letras”, mas é garantido que tenha ao menos uma letra e que tenha no máximo 200 caracteres no total.

#Saída
#Para cada caso de teste, imprima uma linha contendo a(s) letra(s) que mais ocorreu(ocorreram) no texto em 
#minúsculas (se houver empate, imprima as letras em ordem alfabética).

testes = int(input())

for teste in range(testes):
    palavra = input().lower()
    caracteres = {}
    for c in palavra:
        if c.isalpha() and c not in caracteres:
            caracteres[c] = palavra.count(c)

    caracteres_ordenados = sorted(caracteres.items(), key=lambda x: (-x[1],x[0]))
    maior = caracteres_ordenados[0][1]
    resultado = ''
    for c in caracteres_ordenados:
        if c[1] == maior:
            resultado += c[0]
        else:
            break
    print(resultado)