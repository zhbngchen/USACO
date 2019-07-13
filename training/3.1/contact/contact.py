"""
PROG: contact
LANG: PYTHON3

"""
import sys
with open('contact.in', 'r') as fin:
  lines = fin.readlines()

A, B, N = map(int, lines[0].split())

inputs = ''
for i in range(1, len(lines)):
    inputs += lines[i].rstrip()

strCounts = {}
for i in range(A, B+1):
    for j in range(0, len(inputs)-i+1):
        if inputs[j:j+i] not in strCounts.keys():
            strCounts[inputs[j:j+i]] = 1
        else:
            strCounts[inputs[j:j+i]] += 1


countsStr = {}
for key, val in strCounts.items():
    if val not in countsStr.keys():
        countsStr[val] = {}
        countsStr[val][len(key)] = [key]
    elif len(key) not in countsStr[val].keys():
        countsStr[val][len(key)] = [key]
    else:
        countsStr[val][len(key)].append(key)

counts = list(countsStr.keys())
counts = sorted(counts, reverse = True)

with open('contact.out', 'w') as fout:
    for count in counts:
        first = False
        fout.write(str(count) + '\n')
        lenKeys = list(countsStr[count].keys())
        lenKeys = sorted(lenKeys)
        i = 0
        for lenKey in lenKeys:
            if first == False:
                countsStr[count][lenKey].sort()
                for key in countsStr[count][lenKey]:
                    if i == 0:
                        fout.write(key)
                    else:
                        fout.write(' ' + key)
                    i += 1
                    if i == 6:
                        fout.write('\n')
                    i %= 6
                first = True
            else:
                countsStr[count][lenKey].sort()
                for key in countsStr[count][lenKey]:
                    if i == 0:
                        fout.write(key)
                    else:
                        fout.write(' ' + key)
                    i += 1
                    if i == 6:
                        fout.write('\n')
                    i %= 6
        if i != 0:
            fout.write('\n')
        N -= 1
        if N == 0:
            break
