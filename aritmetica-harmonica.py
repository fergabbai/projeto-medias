notas = []

while True:
    nota = float(input('Insira a nota do aluno: '))
    notas.append(nota)

    resposta = int(input('Inserir nova nota? (1-Sim 2-Nao): '))
    if resposta == 2:
        break

calculo = int(input('Qual media deseja calcular? (1-Aritmetica 2-Harmonica): '))

if calculo == 1:
    media_aritmetica = sum(notas) / len(notas)
    print('A media aritmetica do aluno é {:.2f}'.format(media_aritmetica))

elif calculo == 2:
    denominador = [1/nota for nota in notas]
    media_harmonica = len(notas)/sum(denominador)
    print('A media harmonica do aluno é {:.2f}'.format(media_harmonica))

else:
    print('Opcao inválida!\nQual media deseja calcular? (1-Aritmetica 2-Harmonica): ')