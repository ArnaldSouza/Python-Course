# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:14:18 2021

@author: Arninho
"""


#Dada uma expressão qualquer com parênteses, indique se a quantidade de
#parênteses está correta ou não, sem levar em conta o restante da 
#expressão. Por exemplo:
#a+(b*c)-2-a        está correto
#(a+b*(2-c)-2+a)*2  está correto
#enquanto
#(a*b-(2+c)         está incorreto
#2*(3-a))           está incorreto
#)3+b*(2-c)(        está incorreto
#Ou seja, todo parênteses que fecha deve ter um outro parênteses que 
#abre correspondente e não pode haver parênteses que fecha sem um previo
#parenteses que abre e a quantidade total de parenteses que abre e fecha
#deve ser igual.
#Entrada
#Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas 
#com até 1000 caracteres.
#Saída
#O arquivo de saída deverá ter a quantidade de linhas correspondente 
#ao arquivo de entrada, cada uma delas contendo as palavras correct ou 
#incorrect de acordo com as regras acima fornecidas

while True:
    try:
        List1 = input()
        List2 = []
        correct = False
        P1 = 0
        P2 = 0
        for v in List1:
            if (v == '('):
                P1 += 1
                List2.append(v)
            if (v == ')'):
                P2 += 1
                List2.append(v)
        if(len(List2)%2 != 0):
            correct = False
        else:
            if(List2[0] == ')'):
                correct = False
            else:
                if (List2[len(List2) - 1] == '('):
                    correct = False
                else:
                    if (P1 != P2):
                        correct = False
                    else:
                        correct = True
        if(correct):
            print("correct")
        else:
            print("incorrect")
    except (EOFError):
        break