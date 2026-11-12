while True:
    print('1 - Dizer olá')
    print('2 - Sair')
    opcao = input('Escolha: ')

    if opcao == '1':
        print('Olá!')
    elif opcao == '2':
        print('Até logo!')
        break
    else:
        print('Opção inválida.')