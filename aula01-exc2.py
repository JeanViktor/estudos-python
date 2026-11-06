
from datetime import date

ano_atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano
if ano > ano_atual:
    print('Ano de nascimento inválido.')
elif idade >= 18:
    print(f'Sua idade é {idade}, e você já atingiu a maioridade.')
else:
    print(f'Sua idade é {idade}, e você ainda não chegou na maioridade.')