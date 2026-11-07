"""
soma = 0
for numero in range(1, 11):
    soma = soma + numero
print(soma)

"""

numero = int(input('Digite um número para saber sua tabuada: '))
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero}x{i}={resultado}')