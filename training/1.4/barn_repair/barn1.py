"""
PROG: barn1
LANG: PYTHON3
"""

import sys

fin = open("barn1.in", "r")
fout = open ('barn1.out', 'w')

M, S, C = map(int, fin.readline().split())
numbers = []
for i in range(C):
  numbers.append(int(fin.readline()))

numbers.sort()
#print(numbers)

gaps = []
for i in range(C-1):
  gaps.append(numbers[i+1] - numbers[i])

#print(gaps)
#print(len(gaps))

boards = ['B'] + gaps + ['B']
#print(boards)

if C > M:
  total = 0
  gap = 1
  while C > M:
    newBoards = []
    boardExist = False
    goalReached = False
    for i in range(len(boards)-1):
      if boards[i] == gap:
        total += gap #count the removed ones only (without the final M boards)
        C -= 1
        if C == M:
          goalReached = True
          break

        # add 'B' if no previous/next 'B'
        if boards[i-1] == 'B':
          boardExist = True
        elif boards[i+1] != gap and boards[i+1] != 'B' and boardExist == False:
          newBoards.append('B')
      else:
        boardExist = False
        if boards[i] != 'B' or boards[i+1] != 'B': #combine continuous 'B's
          newBoards.append(boards[i])
    if goalReached == True:
      break
    newBoards.append(boards[-1])
    #print("gap=", gap, " C=", C, " total=", total, " newBoards=", newBoards)
    boards = newBoards
    gap += 1
  fout.write(str(total + M) + '\n')
else:
  fout.write(str(C) + '\n')

fout.close()

