while True:
    notas = []
    pesos = []


    def calcular_aritmetica(notas):
        return sum(notas) / len(notas)

    def calcular_ponderada(notas, pesos):
        soma_notas = sum(nota * peso for nota, peso in zip(notas, pesos))
        soma_pesos = sum(pesos)
        return soma_notas / soma_pesos

    def calcular_harmonica(notas):
        soma_inversos = sum(1 / nota for nota in notas)
        return len(notas) / soma_inversos


    while True:
        while True:
            nota = float(input('Insira a nota do aluno: '))
            notas.append(nota)

            confirmar = int(input('Nota: {:.2f}\nConfirmar nota? (1-Sim 2-Nao): '.format(nota)))
            if confirmar == 1:
                break

        resposta = int(input('Inserir nova nota? (1-Sim 2-Nao): '))
        if resposta == 2:
            break

    calculo = int(input('Qual media deseja calcular? (1-Aritmetica 2-Ponderada 3-Harmonica): '))

    if calculo == 1:
        media = calcular_aritmetica(notas)
        print("A média aritmética é {:.2f}".format(media))

    elif calculo == 2:
        while len(pesos) != len(notas):
            peso = float(input("Digite o peso para a nota {}: ".format(len(pesos) + 1)))
            pesos.append(peso)
        media = calcular_ponderada(notas, pesos)
        print("A média ponderada é {:.2f}".format(media))

    elif calculo == 3:
        media = calcular_harmonica(notas)
        print("A média harmonica é {:.2f}".format(media))

    else:
        print('Opcao inválida!\nQual media deseja calcular? (1-Aritmetica 2-Ponderada 3-Harmonica): ')

    nova_resposta = int(input('Novo calculo? (1-Sim 2-Nao): '))

    if nova_resposta == 2:
       break