# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 00:14:01 2021

@author: Arninho
"""
#Problema:

#A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

#- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
#Entrada

#A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
#Saída

#Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".


π = 3.14159
R = float(input())
A = (raio * raio) * 3.14159
print("A area do círculo é=%0.4f" %A)
   