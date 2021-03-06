"""
PROG: barn1
LANG: PYTHON3
"""

import sys

################### Problem Description #########################
# M -- number of boards (length of boards are unlimited, 1 <= M <= 50
# S -- Total number of stalls, 1 <= S <= 200
# C -- Total number of occupied stalls, 1 <= C <= S
# Then number of C lines that contain occupied stall number
# Goal: Find minimum length of M boards that will cover the C occupied stalls
#################################################################

################### Sample Data and Solution ####################
# Summary of solution: Merge gaps into boards from smallest gap size up 
# till number of gaps is equal to M-1
#
# M = 4, S = 50, C = 18
# 3, 4, 6, 8, 14, 15, 16, 17, 21, 25, 26, 27, 30, 31, 40, 41, 42, 43
#
# 18 stalls with 17 gaps in between
#  1, 2, 2, 6,   1, 1,  1,  4,  4,   1,  1,  3,  1,  9,  1,  1,  1
# starting from gap size 1 (increment by 1), remove the gaps (if gap size matches)
# till number of gaps reaching M-1 (M boards with M-1 gaps). 
# At the same time count total size of the remove gaps.
# At the end, the result will be the total size of the removed gaps plus M.
# Data after gap size 1 is removed:
#   total = 10, gaps are: 2, 2, 6, 4, 4, 3, 9
# Data after gap size 2 is removed:
#   total = 14, gaps are 6, 4, 4, 3, 9
# Data after gap size 3 is removed:
#   total = 17, gaps are 6, 4, 4, 9
# Now after removing one gap size 4, number of gaps is equal to M-1=3, and data are:
#   total = 21, gaps are 6, 4, 9
# Final answer is: total + M = 21 + 4 = 25
#
# Note: Easiest way of removing items from the list is to create a new and copy only left items
#################################################################

fin = open("barn1.in", "r")
fout = open ('barn1.out', 'w')

M, S, C = map(int, fin.readline().split())
numbers = []
for i in range(C):
  numbers.append(int(fin.readline()))

numbers.sort()
print(numbers)

gaps = []
for i in range(C-1):
  gaps.append(numbers[i+1] - numbers[i])

print(gaps)
print(len(gaps))

boards = gaps
print(boards)

if C > M:
  total = 0
  gap = 1
  while C > M:
    newBoards = []
    goalReached = False
    for i in range(len(boards)):
      if boards[i] == gap:
        total += gap #count the removed ones only (without the final M boards)
        C -= 1
        if C == M:
          goalReached = True
          break

      else:
        newBoards.append(boards[i])
    if goalReached == True:
      break
    print("gap=", gap, " C=", C, " total=", total, " newBoards=", newBoards)
    boards = newBoards
    gap += 1
  fout.write(str(total + M) + '\n')
else:
  fout.write(str(C) + '\n')

fout.close()

