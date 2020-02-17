# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:51:27 2020

@author: Informatica
"""

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}


book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'


# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
titulo1 = book1.split('by')
titulo1 = titulo1[0]
print(titulo1)
print(len(titulo1))

titulo2 = book2.split('by')
titulo2 = titulo2[0]
print(titulo2)
print(len(titulo2))

titulo3 = book3.split('by')
titulo3 = titulo3[0]
print(titulo3)
print(len(titulo3))





















