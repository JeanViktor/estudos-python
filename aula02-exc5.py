quantidade = int(input('Quantos números irá digitar? '))
maior = int(input('Qual o primeiro número? '))
menor = maior
for i in range(1, quantidade):
    numero = int(input('Digite o proximo número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'O número maior é {maior}.\nO número menor é {menor}.')