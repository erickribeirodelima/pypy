senha = input('Digite a senha: ')

if not senha:
    print('Você não digitou nada.')
elif senha == '1234':
    print('Acesso realizado com sucesso.')
else:
    print('Senha inválida!')