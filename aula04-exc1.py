
lista = ["comer", "correr", "dormir", "igreja", "cantar"]
print(lista)

print(lista[0])
print(lista[2])

lista[1] = "corrida"
print(lista)

# print(lista[5])

print(len(lista))

lista.append("futebol")
print(lista)


nova_lista = []

for i in range(1, 4):
    item = input('Digite o item: ')
    nova_lista.append(item)
print(nova_lista)