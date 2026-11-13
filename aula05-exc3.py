# print('Lista de Filmes\n')

# filmes = []

# while True:
#     print('1 - Adicionar filme.')
#     print('2 - Ver filmes.')
#     print('3 - Remover filmes.')
#     print('4 - Sair.\n')
#     opcao = input('Escolha: ')

#     if opcao == '1':
#         filme = input('Qual o nome do filme? ')
#         filmes.append(filme)
#     elif opcao == '2':
#         numero = 1
#         for filme in filmes:
#             print(f'Filme {numero}: {filme}')
#             numero = numero + 1
#     elif opcao == '3':
#         print('Você escolheu remover um filme.')
#     elif opcao == '4':
#         print('Até logo!')
#         break
#     else:
#         print('Opção inválida.')

print('Lista de Jogos\n')

jogos = []

while True:
    print('1 - Adicionar jogo.')
    print('2 - Ver jogos.')
    print('3 - Remover jogos.')
    print('4 - Sair.\n')
    opcao = input('Escolha: ')

    if opcao == '1':
        jogo = input('Qual o nome do jogo? ')
        jogos.append(jogo)
    elif opcao == '2':
        numero = 1
        if len(jogos) == 0:
            print('Você não adicionou nenhum jogo.')
        for jogo in jogos:
            print(f'{numero} - {jogo}')
            numero = numero + 1
    elif opcao == '3':
        print('Você escolheu remover um jogo.')
    elif opcao == '4':
        print('Até logo!')
        break
    else:
        print('Opção inválida.')