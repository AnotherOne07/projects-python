def cadastrarAluno(alunos, mat):
    NewMat = mat+1
    NewName = input("Digite o nome: ")
    NewTur = int(input("Digite o código da turma: "))
    Notes = []
    for x in range(4):
        while True:
            nt = float(input("Digite a nota "+str(x+1)+": "))
            if nt > 0 and nt <= 10:
                break
            else:
                print("Nota inválida! Digite novamente!")
        Notes.append(nt)
    NewFaltas = int(input("Digite o número de faltas: "))

    NewAln = dict(nome=NewName, turma=NewTur, notas=Notes, faltas=NewFaltas)

    alunos[NewMat] = NewAln

    return [alunos, NewMat]


#cadastrarAluno({},20220001)