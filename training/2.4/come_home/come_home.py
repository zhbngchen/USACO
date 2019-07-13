"""
PROG: comehome
LANG: PYTHON3

"""
import sys

with open("comehome.in", "r") as fin:
  lines = fin.readlines()

N = int(lines[0])

graphs = {}
for i in range(1, N+1):
    x, y, v = lines[i].split()
    v = int(v)
    if x not in graphs.keys():
        graphs[x] = {}
        graphs[x][y] = v
    else:
        if y in graphs[x].keys():
            if graphs[x][y] > v:
                graphs[x][y] = v
        else:
            graphs[x][y] = v
    if y not in graphs.keys():
        graphs[y] = {}
        graphs[y][x] = v
    else:
        if x in graphs[y].keys():
            if graphs[y][x] > v:
                graphs[y][x] = v
        else:
            graphs[y][x] = v

#print(graphs)
def printList(lists):
    for l in lists:
        print(l)

#printList(matrix)
for k in graphs.keys():
    for i in graphs.keys():
        for j in graphs.keys():
            if k in graphs[i].keys() and graphs[i][k] != 0 and k in graphs[j].keys() and graphs[j][k] != 0 and i != j:
                if j in graphs[i] and graphs[i][j] > graphs[i][k] + graphs[j][k] or j not in graphs[i]:
                    graphs[i][j] = graphs[i][k] + graphs[j][k]

#printList(matrix)

resultC = ''
resultL = sys.maxsize
for cow in graphs.keys():
    if ord(cow) >= ord('A') and ord(cow) < ord('Z'):
        if resultL > graphs[cow]['Z']:
            resultL = graphs[cow]['Z']
            resultC = cow

with open('comehome.out', 'w') as fout:
  fout.write(resultC + ' ' + str(resultL) + '\n')
