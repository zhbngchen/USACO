"""
PROG: gift1
LANG: PYTHON3
"""

import sys

fin = open("gift1.in", "r")
fout = open ('gift1.out', 'w')

NP = int(fin.readline())
listName = []
for i in range(NP):
  listName.append(fin.readline().strip())

dictNameNum = {}
for name in listName:
  dictNameNum[name] = 0

while(True):
  giver = fin.readline().strip()
  if giver == '':
    break
  money, num = map(int, fin.readline().split())
  localListName = []
  if num != 0:
    for i in range(num):
      localListName.append(fin.readline().strip())
    modNum = money % num
    dictNameNum[giver] += modNum
    dictNameNum[giver] -= money
    eachAmount = (money - modNum) / num
    for name in localListName:
      dictNameNum[name] += eachAmount
   
for name in listName:
  fout.write(name + ' ' + str(int(dictNameNum[name])) + '\n')

fout.close()
