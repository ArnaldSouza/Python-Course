# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:06:14 2021

@author: Arninho
"""

# 0 - Revisão
# interpretador
# operações numéricas
# operadores lógicos (==, !=, >, >=, <, <=, and, or e not)
# strings
# condicional: if (indentação)

# ###########################################################################
# 1) listas: dos tipos cmpostos talvez o mais versátil.
# ###########################################################################
pares = [0, 2, 4, 6, 8, 10]
print(pares)

# 1.1) indexação -------------------------------------
print(pares[0])
print(pares[1])
print(len(pares))
print(pares[len(pares)-1])
print(pares[len(pares)])

print(pares[2:])

pares + [12, 14, 16]
#pares  = pares + [12, 14, 16]

pares.append(13)
pares[6]
pares[6] = 12

# 1.2) slicing -------------------------------------
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letras[2:4] = ['C', 'D']
letras[2:4] = []

l2 = letras[:] # cópia da lista

# 1.2) listas de listas -------------------------------
comida = [['maçã', 'banana', 'uva'], ['arroz', 'feijão', 'massa', 'batata']]
len(comida)
comida[0]
comida[1]
len(comida[0])
len(comida[1])

comida[1][0]

# ###########################################################################
# 2) relembrando if
nota = float(input("Digite sua nota: "))
if nota >= 8 and  nota <= 10:
    print("caraca muleke! mandou bem!")
elif nota >= 6 and nota < 8:
    print("de boas")
elif nota < 6 and nota >=0:
    print("sabe de nada inocente")
else:
    print("vamo parar com a patifaria!!")

# e se a nota for 8?

# if inline
msg = "belê" if nota>=6 else "mandou mauz"
   

# ###########################################################################
# 3) laços  - for e while

# exemplo fibonacci:
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# percorre uma sequência qualqer
frutas = ['maçã', 'banana', 'uva']
for fruta in frutas:
    print(fruta, len(fruta))

# para sequência de números usar a função range()
for i in range(5):
    print(i, i*i)

for i in range(6, 13, 2):
    print(i)

for i in range(60, 0, -10):
    print(i)

#enumerate: retorna índice e o elemento
for i in range(len(frutas)):
    print(i, frutas[i])

for i, fruta in enumerate(frutas):
    print(i, fruta)

#break e continue
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)
    if i > 6:
        break

# ###########################################################################
# 3) funções

# definindo uma função
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b

#chamando a função
fib(900)

# agora uma função com retorno
def fib_r(n=400):
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a+b
    return res

def fib_r(n):
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a+b
    return res
# testando:
f400 = fib_r()
f150 = fib_r(150)


# search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. Perhaps you’d like to write a small custom database, or a specialized GUI application, or a simple game.
