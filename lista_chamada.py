while True:
    print("E.E. Bibliotecária Maria Antonieta Ferraz \nLista de chamada:")    
    pesquisa = input("\nPara Pesquisar o nome e RA do aluno:\nEscolha [sim] para realizar a pesquisa \nou\nEscolha [não] para encerrar o programa: \nDigite aqui sua decisão: ").strip().lower()
    
    if pesquisa == 'sim':
        try:
            n = int(input("\nDigite seu número da lista de chamada: "))

            match n:
#                Exemplo de como deve ser preenchido!!!   
#                case 1:
#                    print(f"Nº [{n}] Nome: Alisson Ferreira - RA: 000974093649sp")
#                    print()

                case 1:
                    print("Não Participou da Atividade")
                    printf()
                case 2:
                    print("Não Participou da Atividade")
                    print()
                case 3:
                    print("Não Participou da Atividade")
                    print()
                case 4:
                    print("Não Participou da Atividade")
                    print()
                case 5:
                    print(f"[{n}] Nome: Daniel Pereira  - RA:00001116817056")
                
                    print()
                case 6:
                    print("não participou da atividade ")
                    print()
                case 7:
                    print("Não Participou da Atividade")
                    print()
                case 8:
                    print(f"[{n}] nome: Evelyn Diana - RA: 0000110400785")
                    print()
                case 9:
                    print("Não Participou da Atividade")
                    print()
                case 10:
                    print("Não Participou da Atividade")
                    print()
                case 11:
                    print("Não Participou da Atividade")
                    print()
                case 12:
                    print("Não Participou da Atividade")
                    print()
                case 13:
                    print("Não Participou da Atividade")
                    print(f"[{n}] Nome: Gabriel Slater _ RA: 00001093772037")
                case 14:
                    print("Não Participou da Atividade")
                    print()
                case 15:
                    print(f"[n] Nome: Giovanna Vitoria - RA: 00001083033487")
                    print()
                case 16:
                    print("Não Participou da Atividade")
                    print()
                case 17:
                    print("Não Participou da Atividade")
                    print()
                case 18:
                    print("Não Participou da Atividade")
                    print()
                case 19:
                    print(f"[{n}] Nome: Lucas Almeida - RA: 0001124858647")
                    print()
                case 20:
                    print(f"Nº [{n}] Nome: Lucas de Melo Faria - RA: 00001092165502")
                    print()
                case 21:
                    print("Não Participou da Atividade")
                    print()
                case 22:
                    print(f"[{n}] Nome: Milena Dias - RA: 00001103602792")
                    print()
                case 23:
                    print("Não Participou da Atividade")
                    print()
                case 24:
                    print(f"[{n}] Nome: Stheffany Nathany - RA:0001128653")
                    print()
                case 25:
                    print("Não Participou da Atividade")
                    print()
                case 26:
                    print("Não Participou da Atividade")
                    print()
                case 27:
                    print(f"[{n}] Nome: Marcel Ferreira - RA:00001116823871")
                    print()
                case 28:
                    print("Não Participou da Atividade")
                    print()
                case 29:
                    print("Não Participou da Atividade")
                    print()
                case 30:
                    print("Não Participou da Atividade")
                    print()
                case 31:
                    print("Não Participou da Atividade")
                    print()
                case 32:
                    print(f"[{n}] Nome: Arthur Mesquita - RA:0001103895618")
                    print()
                case 33:
                    print("Não participou da atividade")
                    print()
                case 34:
                    print("Não Participou da Atividade")
                    print()
                case 35:
                    print(f"[{n}] Nome: Jorge Miguel - RA: 000109318431")
                    print()
                case 36:
                    print(f"[{n}]" Nome: Stheffany Nathany - RA: 000112967714sp")
                    print()
                case 37:
                    print(f"[{n}] Nome: Richard Da Macena - RA: 00001113150312")
                    print()
                case 38:
                    print("Não Participou da Atividade")
                    print()
                case 39:
                    print("Não Participou da Atividade")
                    print()               
                case 40:
                    print("Não Participou da Atividade")
                    print()
                    
                case _:
                    print("\n\nNúmero de chamada não encontrado.\n\n")

        except ValueError:
            print("\n\nErro: Por favor, insira um número inteiro válido.\n\n")

    elif pesquisa == 'não' or pesquisa == 'nao':
            print("\n\nObrigado pela preferência e volte sempre ;)\n\n")
            break
    else:
        print("\n\nOpção inválida, por favor, digite 'sim' ou 'não'.\n\n")