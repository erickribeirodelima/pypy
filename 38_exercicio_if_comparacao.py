# Faça um exercício de if e comparação

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor=} é menor que o {segundo_valor=}')
else:
    print(f'{primeiro_valor=} é igual o {segundo_valor=}')