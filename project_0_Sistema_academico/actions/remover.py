def removeraluno(alunos,mat):
    alunos.pop(mat)

    return alunos

def buscaaluno(alunos,mat):
    achou = False
    for aln in alunos.keys():
        if aln == mat:
            achou = True
            break
    return achou

