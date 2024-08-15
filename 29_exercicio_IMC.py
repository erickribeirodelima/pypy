# Exercício de IMC

nome = 'Erick Ribeiro'
altura = 1.84
peso = 84
imc = peso / (altura * altura)

print(f'{nome} tem {altura} de altura e pesa {peso} kg.')
print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Seu IMC é abaixo da normalidade.')
elif imc >= 18.5 or imc <= 24.9:
    print('Seu IMC está dentro da normalidade.')
elif imc > 24.9 or imc <= 29.9:
    print('Seu IMC está em Sobrepeso.')
elif imc > 29.9 or imc <= 39.9:
    print('Seu IMC está em obesidade.')
else:
    print('Seu IMC está em obesidade grave.')
