total_min = int(input('Digite o total em minutos: '))
horas = total_min // 60
minutos = total_min % 60
if horas == 1:
    print(f'{horas} hora e {minutos} minutos.')
else:
    print(f'{horas} horas e {minutos} minutos.')