# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:00:12 2021

@author: Arninho
"""
#Considerando a entrada de valores inteiros não negativos, ordene estes valores 
#segundo o seguinte critério:

   # Primeiro os Pares
   # Depois os Ímpares

#Sendo que deverão ser apresentados os pares em ordem crescente e depois os 
#ímpares em ordem decrescente.

#Entrada
#A primeira linha de entrada contém um único inteiro positivo N (1 < N < 105) 
#Este é o número de linhas de entrada que vem logo a seguir. As próximas N 
#linhas conterão, cada uma delas, um valor inteiro não negativo.

#Saída
# todos os valores lidos na entrada segundo a ordem apresentada acima.
#Cada número deve ser impresso em uma linha, conforme exemplo abaixo.

n = int(input())

pares = []
impares = []

for i in range (n):
    num = int(input())
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

pares = sorted(pares)
impares = sorted(impares, reverse=True)

for a in range(len(pares)):
    print(pares[a])
for b in range(len(impares)):   
    print(impares[b])

























