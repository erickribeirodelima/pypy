'''
Operador lógico not é usado para inverter expressões
not True = False
not False = True

'''

senha = input('Digite a senha: ')

if not senha:
    print('Você não digitou nada.')
elif senha == '123456':
    print('Acesso realizado com sucesso.')
else:
    print('Senha inválida.')