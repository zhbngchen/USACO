"""
PROG: holstein
LANG: PYTHON3

"""

import sys

with open("holstein.in", "r") as fin:
  lines = fin.readlines()

V = int(lines[0])
minRequirements = list(map(int, lines[1].split()))

print(minRequirements)

G = int(lines[2])
feeds = []
for i in range(G):
  scoopDetails = list(map(int, lines[3+i].split()))
  feeds.append(scoopDetails)

print(feeds)

def generateCombo(ind, lastInCombo, num, total, combo, results):
  if ind == num:
    results.append([i for i in combo])
    return 
  for i in range(lastInCombo+1, total):
    combo.append(i)
    generateCombo(ind+1, i, num, total, combo, results)
    combo.pop()

def subtractList(list1, list2):
  results = []
  for i in range(len(list1)):
    results.append(list1[i] - list2[i])
  print("subtractList results=", results)
  return results

found = False
result = []
dictComboLeft = {}
print("G=", G)
for i in range(1, G+1):
  combo = []
  genCombos = []
  generateCombo(0, -1, i, G, combo, genCombos)
  print("i=", i, "genCombos=", genCombos)
  for genCombo in genCombos:
    if i == 1:
      subResult = subtractList(minRequirements, feeds[genCombo[0]])
      if max(subResult) <= 0:
        found = True
        result = genCombo
        break
      dictComboLeft[tuple(genCombo)] = subResult
    else:
      genComboCopy = [i for i in genCombo]
      subtractInd = genCombo.pop() # new subtractInd contains the old genCombo[-1] and genCombo contains the old genCombo[0:-1]
      print("subtractInd=", subtractInd, " genCombo=", genCombo)
      subResult = subtractList(dictComboLeft[tuple(genCombo)], feeds[subtractInd])
      if max(subResult) <= 0:
        found = True
        result = genComboCopy
        break
      dictComboLeft[tuple(genComboCopy)] = subResult
  if found == True:
    break
  print("dictComboLeft=", dictComboLeft)

with open('holstein.out', 'w') as fout:
  fout.write(str(len(result)))
  for i in result:
    fout.write(' ' + str(i+1))
  fout.write('\n')

