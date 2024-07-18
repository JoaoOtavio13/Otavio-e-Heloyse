class Pessoa:
  def __init__(self, nomep, cpfp, enderecop):
    self.nome = nomep
    self.__cpf = cpfp
    self.__endereco = enderecop

  def getAtributos(self):
    print('> Nome: {}\n> CPF>: {}\n> endereço:{}'.format(self.__nome, self.__cpf, self.__endereco))


  def Falar(self):
    print('olá!')

