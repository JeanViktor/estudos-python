print('Gerenciador de Tarefas\n')

while True:
    print('1 - Adicionar tarefa.')
    print('2 - Ver tarefas.')
    print('3 - Remover tarefas.')
    print('4 - Sair.\n')
    opcao = input('Escolha: ')

    if opcao == '1':
        print('Você escolheu adicionar.')
    elif opcao == '2':
        print('Você escolheu ver.')
    elif opcao == '3':
        print('Você escolheu remover.')
    elif opcao == '4':
        print('Até logo!')
        break
    else:
        print('Opção inválida.')
