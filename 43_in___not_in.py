nome = input('Digite seu nome: ')
encontrar = input('O que você quer encontrar? ')

if encontrar in nome:
    print(f'{encontrar} existe em {nome}')
else:
    print(f'{encontrar} não existe em {nome}')