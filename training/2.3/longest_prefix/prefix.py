"""
PROG: prefix
LANG: PYTHON3

"""
import sys

with open("prefix.in", "r") as fin:
  lines = fin.readlines()

index = 0
setPrim = []
while True:
    strings = lines[index].strip().split()
    index += 1
    if strings[0] == '.':
        break
    for string in strings:
        setPrim.append(string)

print("setPrim= ", setPrim)

S = ''
while index < len(lines):
    S += lines[index].strip()
    index += 1
print("S= ", S)
print("len(S)= ", len(S))
index = 1
statusS = [0] * len(S)
statusS[0] = 1
while index < len(S):
    if statusS[index-1] == 0:
        index += 1
        continue
    found = False
    for sizeStr in range(1, 11):
        if index + sizeStr > len(S):
            break
        elif statusS[index+sizeStr-1] == 1:
            found = True
        elif S[index:(index+sizeStr)] in setPrim:
            statusS[index+sizeStr-1] = 1
            found = True
    if found == False:
        break
    index += 1


print("index= ", index)
with open('prefix.out', 'w') as fout:
  fout.write(str(index) + '\n')

