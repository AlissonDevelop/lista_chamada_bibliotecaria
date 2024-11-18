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
                    print()
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
                    print("Não Participou da Atividade")
                    print()
                case 6:
                    print("Não Participou da Atividade")
                    print()
                case 7:
                    print("Não Participou da Atividade")
                    print()
                case 8:
                    print("Não Participou da Atividade")
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
                    print()
                case 14:
                    print("Não Participou da Atividade")
                    print()
                case 15:
                    print("Não Participou da Atividade")
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
                    print("Não Participou da Atividade")
                    print()
                case 20:
                    print(f"Nº [{n}] Nome: Lucas de Melo Faria - RA: 00001092165502")
                    print()
                case 21:
                    print("Não Participou da Atividade")
                    print()
                case 23:
                    print("Não Participou da Atividade")
                    print()
                case 24:
                    print("Não Participou da Atividade")
                    print()
                case 25:
                    print("Não Participou da Atividade")
                    print()
                case 26:
                    print("Não Participou da Atividade")
                    print()
                case 27:
                    print("Não Participou da Atividade")
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
                    print("Não Participou da Atividade")
                    print()
                case 33:
                    print("Não Participou da Atividade")
                    print()
                case 34:
                    print("Não Participou da Atividade")
                    print()
                case 35:
                    print(f"[{n}] Nome: Jorge Miguel - RA: 000109318431")
                    print()
                case 36:
                    print("Não Participou da Atividade")
                    print()
                case 37:
                    print("Não Participou da Atividade")
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