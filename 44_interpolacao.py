"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = 'Erick'
preco = 1000.987500
variavel = '%s, o preço é %f' % (nome, preco)
print(variavel)

sobrenome = 'Ribeiro'
idade = 35
variavel2 = '%s, seu sobrenome é %s e sua idade é %i anos' % (nome, sobrenome, idade)
print(variavel2)