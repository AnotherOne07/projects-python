def mostrarmenu(alunos):
    option = 0
    while option >= 0:
        print("1 - Listar todos: ")
        print("2 - Listar por turma")
        print("3 - Listar reprovados por média")
        print("4 - Listar reprovados por falta")
        print("5 - Listar os aprovados")
        print("Digite -1 para sair.")
        option = int(input("Selecione uma das opções acima: "))

        if option == 1:
            listartodos(alunos)
        elif option == 2:
            turma = int(input("Informe a turma: "))
            listarturma(alunos, turma)
        elif option == 3:
            turma = int(input("Informe a turma: "))
            listarreprovadosmedia(alunos, turma)
        elif option == 4:
            turma = int(input("Informe a turma: "))
            listarreprovadosfalta(alunos, turma)
        elif option == 5:
            turma = int(input(("Informe a turma: ")))
            listaraprovados(alunos, turma)
        elif option == -1:
            break
        else:
            print("ERRO! Opção selecionada é inválida!")


def listartodos(alunos):
    print("ALUNOS CADASTRADOS")
    print("Nome Turma Faltas Notas")
    for aln in alunos:
        print("{0} {1} {2} {3} {4} {5} {6}".format(alunos[aln]["nome"], alunos[aln]["turma"],alunos[aln]["faltas"],alunos[aln]["notas"][0],alunos[aln]["notas"][1],alunos[aln]["notas"][2],alunos[aln]["notas"][3]))


def listarturma(alunos, turma):
    print("ALUNOS CADASTRADOS")
    print("Nome Turma Faltas Notas")
    for aln in alunos:
        if alunos[aln]["turma"] == turma:
            print("{0} {1} {2} {3} {4} {5} {6}".format(alunos[aln]["nome"], alunos[aln]["turma"], alunos[aln]["faltas"], alunos[aln]["notas"][0], alunos[aln]["notas"][1], alunos[aln]["notas"][2], alunos[aln]["notas"][3]))


def listaraprovados(alunos, turma):
    print(("ALUNOS APROVADOS"))
    print("Nome Turma Faltas Média")
    for aln in alunos:
        if alunos[aln]["turma"] == turma:
            medialuno = calculamedia(alunos[aln]["notas"])
            if alunos[aln]["faltas"] <= 30 and medialuno >= 7:
                print("{0} {1} {2} {3}".format(alunos[aln]["nome"], alunos[aln]["turma"], alunos[aln]["faltas"], medialuno))


def listarreprovadosmedia(alunos, turma):
    print("ALUNOS REPROVADOS POR MÉDIA")
    print("Nome Turma Faltas Média")
    for aln in alunos:
        if alunos[aln]["turma"] == turma:
            medialuno = calculamedia(alunos[aln]["notas"])
            if medialuno < 7:
                print("{0} {1} {2} {3}".format(alunos[aln]["nome"], alunos[aln]["turma"], alunos[aln]["faltas"], medialuno))

def listarreprovadosfalta(alunos, turma):
    print("ALUNOS REPROVADOS POR FALTA")
    print("Nome Turma Frequência")
    for aln in alunos:
        if alunos[aln]["turma"] == turma:
            freq = calculafrequencia(alunos[aln]["faltas"])
            if freq < 60:
                print("{0} {1} {2:.2f}".format(alunos[aln]["nome"], alunos[aln]["turma"], freq))

def calculamedia(notas):
    total = 0.0
    for nt in notas:
        total += nt
    media = total/4
    return media

def calculafrequencia(faltas):
    freq = (75 - faltas)/75
    return freq*100

