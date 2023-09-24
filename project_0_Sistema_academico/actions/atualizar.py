def mostraaluno(alunos, matricula):
    aln = alunos[matricula]
    notes = aln['notas']
    print("Dados Atuais: ")
    print("Nome: {} || Turma: {} || Faltas: {}".format(aln['nome'], aln['turma'], aln['faltas']))
    print("Notas: {} {} {} {}".format(notes[0], notes[1], notes[2], notes[3]))


def alterardados(notas):
    i = 0
    while i<4:
        notas[i] = float(input("Digite a nota {}: ".format(i+1)))
        i+=1

    faltas = int(input("Digite as faltas: "))

    return [notas,faltas]


def atualizaaluno(alunos, matricula):

    mostraaluno(alunos, matricula)
    [alunos[matricula]["notas"], alunos[matricula]["faltas"]] = alterardados(alunos[matricula]["notas"])

    return alunos