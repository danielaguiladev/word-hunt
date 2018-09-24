"""
  author: Daniel Soares Aguila
  email: danielaguila_96@hotmail.com
  Processo seletivo prova backend studiosol
"""

class MyIterator(object):
    def __init__(self, a, n, h0=0, v0=0, h=1, v=1, flow=0):
      """
        Iniciar MyIterator para iterar em etapas

        :param m: matriz.
        :type m: list[list[str]]
        :param n: Numero de iteracoes.
        :type n: int
        :param h0: Posicao horizontal inicial na matriz.
        :type h0: int
        :param v0: Posicao vertical inicial na matriz.
        :type v0: int
        :param h: Direcao horizontal.
        :type h: int
        :param v: Direcao vertical.
        :type v: int
      """
      super(MyIterator, self).__init__()
      self.a = a
      self.n = n
      self.h0 = h0
      self.v0 = v0
      self.h = h
      self.v = v
      self.flow = flow
    def __iter__(self):
      h = self.h0
      v = self.v0
      aux = 0
      # criterio de parada, se alcancar o tamanho da palavra
      if aux < self.n:
        # lancar posicao
        yield self.a[v][h]
        # incrementar 1
        aux += 1
      try:
        while aux < self.n:
          # se a direcao for vertical
          if self.flow == 1:
            v += self.v
          else:
            h += self.h
          yield self.a[v][h]
          aux += 1
          if aux < self.n:
            if self.flow == 1:
              h += self.h
            else:
              v += self.v
            yield self.a[v][h]
            aux += 1
      except IndexError: return
