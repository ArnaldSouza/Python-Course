    # -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:04:57 2021

@author: Arninho
"""

# 0.1: Porque usar python
# - Uma das linguagens mais populares
# - Muito simples, mas super versátil
# - Desenvolvimento rápido, grande base de usuários e bibliotecas

# 0.2 O que é uma linguagem interpretada

# 1) Usando o interpretador (modo interativo)
# 1.1) calculadora
#    no prompt escreva os exemplos: 
#     5+5
#     2+3*4
#     (2+3)*4
#     4/2
#     4//2
#     10%3
#     4**2

# 1.2) definindo variáveis
quant = 5
type(quant)
preco = 2.5
type(preco)
print(quant)
total = quant * preco
type(total)

# 2) Strings
#    Sequencia de caracteres delimitados por aspas simples (') ou duplas (").
#       exemplos: 
'em briga de saci, todo chute é voadora'
'em briga de saci, todo "chute" é voadora'
"em briga de saci, todo 'chute' é voadora"
'em briga de saci, todo \'chute\' é voadora'

# 2.1) Função print
print("O cara era tão magro que o chuveiro dele só tinha um furo!")
print("O cara era tão magro...\t que o chuveiro dele só tinha um furo!")
print("O cara era tão magro...\n que o chuveiro dele só tinha um furo!")

# 2.2) definindo uma variável string
s = "O cara era tão 'magro'...\nque o chuveiro dele só tinha um furo!"
print(s)
type(s)

# 2.3) concatenando e repetindo
s = s + '\n' + 'k'*5 + "\t por isso é legal"
print(s)

# |S||o||v||a||c||u||d||o|
# |0||1||2||3||4||5||6||7|

# 2.4) indexando
p = "Sovacudo"
print(p[0])
print(p[1])
print(p[2])

print(len(p))

print(p[-1])
print(p[-2])
print(p[-3])

print(p[0:2])
print(p[:2])

print(p[-2:8])
print(p[6:])

print(p[12])

# 2.5) imprimindo valores
idade = 18
type(idade)
print("tenho %d anos de idade" % idade)
print(f"tenho {idade} anos de idade")

# usando % - %d int, %f - float, %s - string
nome = 'João'
idade = 87
peso = 74.5

# notem as casas decimais
print("nome: %s, idade: %d, peso: %.1f" % (nome, idade, peso))
print("nome: %s, idade: %d, peso: %.2f" % (nome, idade, peso))

# input
nome = input('digite seu nome: ')
idade = input('quantos anos vc tem? ')
print(type(idade))
idade_i = int(idade)
print(type(idade_i))
''
# split
nome, sobrenome, idade = input('digite seu nome sobrenome e idade separados por espaço: ').split()


# 3) condicionais
idade_i = 5
responsavel = False
if idade_i > 18 and responsavel: 
    print('já pode dirigir')
    print('mas toma cuidado')
else: 
    print('chora bebezão')

if idade_i > 40: print("tá acabado hein tio") 



#urionlinejugdge
