"""
  author: Daniel Soares Aguila
  email: danielaguila_96@hotmail.com
  Processo seletivo prova backend studiosol
"""

from MyIterator import *

initArray = """D C Y G W R P K H O A B U V H
A N I R F D A M C P M Y C F P
U I E R X T N I O T A S M X C
E J L A G S A E L G L R X A D
K D Z T A D C V J Q M J I N G
D A N Q E A N I A L A L E I V
I N I E X V I E P A L H E T A
L E E L U U T L G U A N L O I
V H I H Z U C I G A A C E I B
A R Z H X A L C D B R E U N A
U N B S T M U N A C I E L A D
W R A U J A E I L S N L L I S
C M E L E N L I E C O L E B E
T N I O T A A N T R E S I N L
D A I K U D D E Q T A M L A D"""

print(initArray, '\n')

def putWordInAnswer(answer, row, column, v, h, flow):
  for x in range(len(word)):
    if x % 2 == 0:
      answer[row][column] = word[x]
      # se a direcao for vertical
      if flow == 1:
        row += h
      else:
        column += v
    else:
      answer[row][column] = word[x]
      if flow == 1:
        column += v
      else:
        row += h
  return answer

def loop(answer, findNumber, flow):
  """
    - direita (→) e abaixo (↓)
    - direita (→) e acima (↑)
    - esquerda (←) e abaixo (↓)
    - esquerda (←) e acima (↑)
    - abaixo (↓) e à direita (→)
    - abaixo (↓) e à esquerda (←)
    - acima (↑) e à direita (→)
    - acima (↑) e à esquerda (←)
  """
  directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
  for x in directions:
    w = ''.join(iter(MyIterator(array, len(word), column, row, x[0], x[1], flow)))
    if w == word:
      findNumber += 1
      answer[row][column] = '*'
      answer = putWordInAnswer(answer, row, column, x[0], x[1], flow)
      print('Encontrado palavra', word, 'na (linha, coluna)', '(',row,',', column,')')
  return answer, findNumber

if __name__ == '__main__':
  # dividir linhas da matriz
  array = [k.split() for k in initArray.upper().splitlines()]

  # Ler palavras
  # Se digitar a palavra DANIEL aparece em todas as direcoes
  words = input('Digite a palavras separadas por virgula ou espaco para a busca: ')

  # Filtrar palavras e verificar se existe algum caracter que nao seja letra
  words = [''.join(filter(str.isalpha, k)) for k in words.upper().split()]

  # numero de linhas
  numberRows = len(array)
  # numero de colunas
  numberColumns = len(array[0])

  # matriz resposta preenchida com pontos
  answer = [["." for _ in range(numberColumns)] for __ in range(numberRows)]

  """
    flow = direcao da iteracao
    0 = horizontal
    1 = vertical
  """
  for flow in range(2):
    for word in words:
      findNumber = 0
      for row in range(numberRows):
        for column in range(numberColumns):
          # direcao direita -> baixo
          (answer, findNumber) = loop(answer, findNumber, flow)
      if findNumber > 0:
        print(findNumber, 'ocorrencias para a palavra', word)
      else:
        print('Nenhuma ocorrencia para a palavra', word)

  # junte cada linha na matriz resposta separada por \n
  print('\n', *(' '.join(k) for k in answer), sep = '\n')
