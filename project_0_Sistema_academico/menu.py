import actions.cadastrar as cadastrar
import actions.listar as listar
import actions.remover as remover
import actions.ordernar as ordernar
import actions.atualizar as atu
import json
import config.carregardados as carregardados

# Inicializando variáveis que serão utilizadas ao longo do programa
#matricula = 2022000
option = 0

#alunos = {2022001: {'nome': 'Francisco', 'turma': 1, 'notas': [10.0, 10.0, 10.0, 10.0], 'faltas': 0}}
# a função list(dicionário)[-1] me permite pegar a última key do meu dicionário
# para que funcione adequadamente, é necessário que as chaves estejam ordenadas
# em ordem crescente
alunos = carregardados.carregadearquivo()
matricula = list(alunos)[-1]


while option != -1:

    print("MENU PRINCIPAL")
    print("1 - Cadastrar aluno")
    print("2 - Remover aluno")
    print("3 - Atualizar aluno")
    print("4 - Listar alunos")
    print("5 - Ordenar registros")
    print("-1 Sair")
    option = int(input("Digite uma das opções acima: "))

    if option == 1:
        print("Cadastrar")
        [alunos, matricula] = cadastrar.cadastrarAluno(alunos, matricula)
        print(alunos)
    elif option == 2:
        print("Remover")
        alnRem = int(input("Informe a matricula do aluno: "))
        if remover.buscaaluno(alunos, alnRem):
            alunos = remover.removeraluno(alunos, alnRem)
        else:
            print("Nenhum aluno encontrado!")
        print(alunos)
    elif option == 3:
        print("Atualizar")
        alnUpd = int(input("Informe a matricula do aluno: "))
        if remover.buscaaluno(alunos, alnUpd):
            alunos = atu.atualizaaluno(alunos, alnUpd)
        else:
            print("Nenhum aluno encontrado!")
    elif option == 4:
        print("Listar")
        listar.mostrarmenu(alunos)
    elif option == 5:
        print("Ordenar registros")
        alunos = ordernar.definirordem(alunos)
    elif option == -1:
        alunos = ordernar.ordempadrao(alunos)
        data = json.dumps(alunos)
        print(data)
        file = open("data/alunos.txt", "w")
        file.write(data)
    else:
        print("Opção inválida! Selecione uma opção disponível no menu")