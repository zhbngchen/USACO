"""
PROG: concom
LANG: PYTHON3

"""
import sys
with open('concom.in', 'r') as fin:
  lines = fin.readlines()

fout = open('concom.out', 'w')

######################################### Problem Description ##########################################
# Inputs: 
#   Line 1: N, number of input triples to follow
#   Line 2..N+1: Three integers per line as a triple (i, j, p).
#                i: controlling company number
#                j: controlled company number
#                p: percentage
# Rules: Company A controls company B if:
#        1. A = B
#        2. A owns more than 50% of B
#        3. A controls K companies C1, ..., Ck with each Ci owning Xi% of B and X1+X2+...+Xk > 50
#           Note for 3: if A owns more than 50% of Ci, Xi is counted toward A owning B
#
# Sample input:
# 6
# 1 2 30
# 2 3 52
# 3 4 51
# 4 5 70
# 5 4 20
# 4 3 20
#
####################################### Solution #####################################################
# Translate sample input to OwnRelations(Percentage of i owning j):
# i/j  0   1   2   3   4   5  
# 0    0   0   0   0   0   0
# 1    0   0  30   0   0   0
# 2    0   0   0  52   0   0
# 3    0   0   0   0  51   0
# 4    0   0   0  20   0  70    
# 5    0   0   0   0  20   0
# 
# Each row represent direct owning relationship.
# In order to get in-direct owning relationship, we need to aggregate multiple rows. 
# For example:
#              Because 2 owns 3 by 52% and 3 owns 4 by 51%, 2 controls 4 by 51%. 
#              Now since 4 owns 5 by 70%, 2 and 4 control 5 by 70%.
#              Actually 2 controls 3 by 72% since 2 got extra 20% of 3 by controlling 4 (not added in actual code because unnecessary).
# From one certain row, we will go to other rows and aggregate the other row if controlling more than 50%.
#####################################################################################################

def print2D(list2D):
  for item in list2D:
    print(item)

size = 101
OwnRelations = [[0 for _ in range(size)] for _ in range(size)]
N = int(lines[0])
for k in range(1, N+1):
  i, j, p = map(int, lines[k].split())
  OwnRelations[i][j] = p
#print("OwnRelations= ")
#print2D(OwnRelations)

def solve(OwnRelations, index, aggregate):
  for i in range(len(OwnRelations)):
    if aggregate[i] > 50:
      continue
    aggregate[i] += OwnRelations[index][i]
    if aggregate[i] > 50:
      solve(OwnRelations, i, aggregate)


for i in range(size):
  aggregate = [0 for _ in range(size)]
  solve(OwnRelations, i, aggregate)
  for j in range(size):
    if aggregate[j] > 50 and j != i:
      fout.write(str(i) + ' ' + str(j) + '\n')

fout.close()
