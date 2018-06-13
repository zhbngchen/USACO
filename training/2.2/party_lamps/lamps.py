"""
PROG: lamps
LANG: PYTHON3

"""
import sys

with open("lamps.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])
C = int(lines[1])
lampsOn = list(map(int, lines[2].split()))
lampsOff = list(map(int, lines[3].split()))

lampsOn.pop() #remove ending -1
lampsOff.pop() #remove ending -1

"""
print("lampsOn=", lampsOn)
print("lampsOff=", lampsOff)

def shrink(value):
  strVal = str(value)
  listVal = sorted(list(strVal))
  retVal = 0
  for i in range(4, 0, -1):
    count = listVal.count(str(i))
    if count % 2 == 1:
      retVal = retVal * 10 + i
  return retVal
  

def createCombo(index, count, result, results):
  if index > count:
    results.add(shrink(result))
    return 
  for i in range(1, 5):
    result = result * 10 + i
    createCombo(index + 1, count, result, results)
    result = result // 10

for count in range(1, 10):
  result = 0
  results = set()
  createCombo(1, count, result, results)
  print("results=", results)
  print("count=", count, " len(results)=", len(results))
"""

actionCombosList = [[['0']], 
          [['1'], ['2'], ['3'], ['4']],
          [['0'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3'], ['2', '4'], ['3', '4']],
          [['1'], ['2'], ['3'], ['4'], ['1', '2', '3'], ['1', '2', '4'], ['1', '3', '4'], ['2', '3', '4']],
          [['0'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3'], ['2', '4'], ['3', '4'], ['1', '2', '3', '4']]]

if C > 4:
  if C % 2 == 0:
    C = 4
  else:
    C = 3

actionCombos = actionCombosList[C]

statesList = []

def pressButton(states, action):
  newStates = []
  if action == '0':
    return states
  elif action == '1':
    for state in states:
      newStates.append(state ^ 1)
  elif action == '2':
    for i in range(len(states)):
      if i%2 == 0:
        newStates.append(states[i] ^ 1)
      else:
        newStates.append(states[i])
  elif action == '3':
    for i in range(len(states)):
      if i%2 == 1:
        newStates.append(states[i] ^ 1)
      else:
        newStates.append(states[i])
  else:
    for i in range(len(states)):
      if i%3 == 0:
        newStates.append(states[i] ^ 1)
      else:
        newStates.append(states[i])
  return newStates
   
for actions in actionCombos:
  states = [1] * N
  for action in actions:
    states = pressButton(states, action)
  statesList.append(states)
  
results = []
for states in statesList:
  match = True
  for lampOn in lampsOn:
    if states[lampOn-1] != 1:
      match = False
      break
  if match == True:
    for lampOff in lampsOff:
      if states[lampOff-1] != 0:
        match = False
        break
  if match == True:
    results.append(states)

results.sort()

with open('lamps.out', 'w') as fout:
  if len(results) == 0:
    fout.write("IMPOSSIBLE\n")
  else:
    for result in results:
      for i in result:
        fout.write(str(i))
      fout.write('\n')

