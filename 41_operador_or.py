"""
Operador or

Qualquer condição verdadeira avalia toda expressão como verdadeira

São considerados falsy (que você já viu) 0 0.0 '' False

Também existe o tipo None que é usado para representar um valor 

"""

entrada = input('[E]ntrar ou [S]air: ')

if entrada == 'E' or entrada == 'e':
    print('Entrada realizada com sucesso.')
elif entrada == 'S' or entrada == 's':
    print('Saida realizada com sucesso.')
else:
    print('Campo digitado não corresponde com as opções.')