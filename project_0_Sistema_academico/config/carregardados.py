import json

def carregadearquivo():
    """""
        Levando em consideração que arquivos JSON apenas armazenam texto, o código
        abaixo faz a "conversão" das chaves MATRICULA que identificam cada registro
        único de aluno no "banco", através da atribuição usando o for, o programa
        vai percorrer todo o dictionário e converter as chaves strings para integer
    """
    try:
      file = open("../data/alunos.txt", "r")
      data = json.loads(file.read())
      bancoalunos = {int(alunomatricula):registro for alunomatricula, registro in data.items()}
      return bancoalunos
    except:
        print("ERRO! Não foi possível carregar dados de alunos")

