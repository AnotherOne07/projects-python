def definirordem(alunos):

    print("1 - Alfabética")
    print("2 - Média")
    print("3 - Frequência")
    print("4 - Matrícula")
    print("-1 para sair")
    option = int(input("Selecione uma das opções acima: "))

    if option == 1:
        return ordemalfabetica(alunos)
    elif option == 2:
        return ordemmedia(alunos)
    elif option == 3:
        return ordemfrequencia(alunos)
    elif option == 4:
        return ordempadrao(alunos)


def ordemalfabetica(alunos):
    # Obtendo a lista de alunos, através do unpacking operator (*)
    listaalunos = [*alunos.keys()]

    nomesalunos = []
    i = 0
    j = 0
    # Iteração para criar lista com nomes e depois ordenar utilizando o método sort()
    while i < len(listaalunos):
        # Primeiro acessa o objeto alunos, encontra o nome para cada matricula e depois adiciona ao final da lista
        nomeAlnPosAt = alunos[listaalunos[i]]["nome"]
        nomesalunos.append(nomeAlnPosAt)
        i += 1
    nomesalunos.sort()

    # Iteração para gerar um novo objeto a partir do original (alunos) utilizando a ordem da lista 'nomesalunos'
    listaOrdenada = {}
    i = 0
    while i < len(listaalunos):
        # Primeira tarefa é identificar qual é matricula do aluno, então criar uma cópia dos dados e adicionar ao novo objeto alunos que será criado
        while j < len(listaalunos):
            if nomesalunos[i] == alunos[listaalunos[j]]["nome"]:
                matAlnAtual = listaalunos[j]
            j += 1

        alnPosAt = alunos[matAlnAtual]
        listaOrdenada[matAlnAtual] = alnPosAt
        i += 1
        j = 0

    return listaOrdenada

def ordempadrao(alunos):
    # Primeiro passo é criar uma lista com as matrículas dos alunos
    listaalunos = [*alunos.keys()]
    listaalunos.sort()

    listaOrdenada = {}
    i = 0
    j = 0
    # Segundo passo é fazer uma iteração através dos índices de listaalunos e atribuir ao novo objeto o respectivo valor presente no objeto original 'alunos'
    while i < len(listaalunos):
        listaOrdenada[listaalunos[i]] = alunos[listaalunos[i]]
        i += 1

    return listaOrdenada

def ordemmedia(alunos):
    notasMatricula = []

    # método que irá receber um array contendo a matrícula e a nota, e retornará a nota
    def returnMedia(objeto):
        return objeto[1]

    for aluno in alunos:
        soma = 0
        # Laço para fazer a soma das notas
        for nota in alunos[aluno]["notas"]:
            soma += nota
        media = soma/4
        alunoAtual = [aluno, media]
        notasMatricula.append(alunoAtual)

    # Através do método sort() do protótipo List do python, passando os paramêtros reverse que define a ordem decrescente
    # e a 'key' que será o critério utilizado para ordenar, a lista será ordenada de acordo com o critério definido
    notasMatricula.sort(reverse=True, key=returnMedia)

    # Criando uma cópia da lista original 'aluno' aplicando a ordem descrescente das notas como critério de ordenação
    listaOrdenada = {}
    for aluno in notasMatricula:
        listaOrdenada[aluno[0]] = alunos[aluno[0]]

    return listaOrdenada

def ordemfrequencia(alunos):

   # Inicializando variável que vai armazenar os pares de dados [matricula, faltas] dos alunos
    matriculaFaltas = []

    # Função que receberá o par de dados e retornará as faltas
    def returnFaltas(object):
        return object[1]

    # Laço para adicionar cada par de dados ao vetor matriculaFaltas
    for aluno in alunos:
        matriculaFaltas.append([aluno, alunos[aluno]["faltas"]])

    # Utilizando o método do protótipo array sort() para ordenar os pares de dados de aluno armazenados na variável
    # matriculaFaltas, que depois será utilizado para gerar uma lista "cópia"
    matriculaFaltas.sort(key=returnFaltas)

    # Inicializando a variável que irá armazenar a "lista cópia"
    listaOrdenada = {}

    # Laço para armazenar os registros na nova lista
    for aluno in matriculaFaltas:
        listaOrdenada[aluno[0]] = alunos[aluno[0]]

    return listaOrdenada
