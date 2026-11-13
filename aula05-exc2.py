print('Gerenciador de Tarefas\n')

tarefas = []

while True:
    print('1 - Adicionar tarefa.')
    print('2 - Ver tarefas.')
    print('3 - Remover tarefas.')
    print('4 - Sair.\n')
    opcao = input('Escolha: ')

    if opcao == '1':
        tarefa = input('Digite a tarefa: ')
        tarefas.append(tarefa)
    elif opcao == '2':
        numero = 1
        if len(tarefas) == 0:
            print('Você não adicionou nenhuma tarefa.')
        for tarefa in tarefas:
            print(f'{numero} - {tarefa}')
            numero = numero + 1
    elif opcao == '3':
        print('Você escolheu remover.')
    elif opcao == '4':
        print('Até logo!')
        break
    else:
        print('Opção inválida.')