from main import Pessoa

class Aluno(Pessoa):
    def __init__(self, nomep, cpfp, enderecop, turmap, cursop):
        Pessoa.__init__(nomep, cpfp, enderecop)
        self.turma= turmap
        self.curso= cursop

    def getTurma(self):
        print(f'Turma: {self.turma}')

    def getCurso(self):
        print(f'Curso: {self.curso}')
