"""
senha = input('Digite a sua senha: ')
while senha != 'xesque':
    print('Senha errada.')
    senha = input('Digite a senha novamente: ')
print('Senha correta.')
"""

soma = 0
numero = int(input('Digite um número: '))
while numero != 0:
    soma = soma + numero
    numero = int(input('Digite mais um número: '))
print(f'{soma}')