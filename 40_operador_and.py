"""
Operadores lógicos
and (e) or (ou) not (não)
and - Todas a condições precisam ser verdadeiras
"""

user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if user == 'erickribeiro' and senha == '123456':
    print("Acesso realizado com sucesso.")
else:
    print("Usuário ou senha incorreto.")