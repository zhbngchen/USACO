"""
PROG: butter
LANG: PYTHON3

"""
import sys
import queue

with open('butter.in', 'r') as fin:
  lines = fin.readlines()

def dijkstra(edges, d, ind):
    q = queue.PriorityQueue()
    q.put([0, ind])
    visited = [False] * P
    while not q.empty():
        cur = q.get()
        #print("q get:", cur[0])
        if visited[cur[1]] == True:
            continue
        for edge in edges[cur[1]]:
            if d[ind][edge[1]] > d[ind][cur[1]] + edge[0]:
                d[ind][edge[1]] = d[ind][cur[1]] + edge[0]
                q.put([d[ind][edge[1]], edge[1]])
                #print("q put:", d[ind][edge[1]])
        visited[cur[1]] = True
    print("ind=", ind)
    for i in range(len(d[0])):
        print(d[ind][i])
    

N, P, C = map(int, lines[0].split())

pastures = []
for i in range(N):
    pastures.append(int(lines[i+1]) - 1)

edges = {}
for i in range(C):
    p1, p2, lenP = map(int, lines[N+1+i].split())
    p1n = p1 - 1
    p2n = p2 -1
    if p1n not in edges.keys():
        edges[p1n] = []
    edges[p1n].append([lenP, p2n])
    if p2n not in edges.keys():
        edges[p2n] = []
    edges[p2n].append([lenP, p1n])
    
d = [[sys.maxsize for i in range(P)] for i in range(P)]

for i in range(P):
    d[i][i] = 0

for i in pastures:
    dijkstra(edges, d, i)

result = sys.maxsize
for i in range(P):
    totalLen = 0
    for pasture in pastures:
        totalLen += d[pasture][i]
        if i == 0:
            print("pasture=", pasture, "d=", d[pasture][i])
    if result > totalLen:
        result = totalLen
        print("i=", i, ", result=", result)

with open('butter.out', 'w') as fout:
    fout.write(str(result) + '\n')

