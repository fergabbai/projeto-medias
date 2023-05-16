# PROJETO MÉDIAS 🧮
## Este projeto consiste em um programa no qual o usuário insere as notas dos alunos (quantas desejar) e escolhe a média que deseja calcular:
### **Aritmética, Ponderada ou Harmonica**
Obs: Para facilitar para o usuário, o programa arredonda todas as notas inseridas para duas casas decimais.
##
### O PROGRAMA
#### O programa inicia com laço de repetição (Laço 1), e são criadas duas variáveis, Notas e Pesos, como listas vazias.
#### São criadas 3 funções para calcular as médias que serão solicitadas a seguir:
#### Aritmética:
Calcula a soma das notas e divide pela quantidade de notas inseridas.
#### Ponderada:
Primeiramente multiplica a nota pelo seu respectivo peso, que será solicitado a frente, soma os resultados e divide pela soma dos pesos.
#### Harmonica:
Primeiramente soma os inversos das notas, em seguida divide a quantidade de notas pela soma dos inversos.
#### São criados mais dois laços de repetição (Laço 2 e Laço 3).
#### No laço 3, solicita ao usuário que insira a nota do aluno. Logo após imprime essa nota arredondando para duas casa decimais e pergunta ao usuário se ele confirma a nota. Caso a resposta seja Não, ele solicita novamente a nota. Caso seja Sim o laço 3 é encerrado.
#### No laço 2, após a nota inserida ser confirmada, o programa pergunta ao usuário se ele deseja inserir uma nova nota. Caso a resposta seja Sim, o programa solicita uma nova nota, voltando ao Laço 2. Caso a resposta seja Não, o Laço 2 é encerrado.
#### O programa solicita ao usuário qual média ele deseja calcular:
##### **1 - Aritmética**
##### **2 - Ponderada**
##### **3 - Harmonica**
#### De acordo com a opção escolhida, o programa calcula a média usando a respectiva função definida acima, e imprime a média do aluno.
#### Feito o cálculo da média escolhida, o programa pergunta ao usuário se ele deseja iniciar um novo cálculo. Caso a resposta seja Sim, o programa é iniciado totalmente. Caso a resposta seja Não, o Laço 1 é encerrado juntamente com o programa.
