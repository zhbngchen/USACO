"""
PROG: butter
LANG: PYTHON3

"""
import sys
import queue

with open('butter.in', 'r') as fin:
  lines = fin.readlines()

N, P, C = map(int, lines[0].split())

pastures = []
for i in range(N):
    pastures.append(int(lines[i+1])-1)

d = [[sys.maxsize for _ in range(P)] for _ in range(P)]

edges = {}
for i in range(C):
    p1, p2, lenP = map(int, lines[N+1+i].split())
    p1n = p1 - 1
    p2n = p2 -1
    if p1n not in edges.keys():
        edges[p1n] = []
    edges[p1n].append([p2n, lenP])
    if p2n not in edges.keys():
        edges[p2n] = []
    edges[p2n].append([p1n, lenP])
    
for i in range(P):
    d[i][i] = 0

def spfa(d, edges, u):
    q = queue.Queue()
    q.put(u)
    visited = [False] * P
    #print("u=", u)
    while not q.empty():
        cur = q.get()
        #print("cur=", cur)
        for edge in edges[cur]:
            if d[u][edge[0]] > d[u][cur] + edge[1]:
                d[u][edge[0]] = d[u][cur] + edge[1]
                if visited[edge[0]] == False:
                    q.put(edge[0])
                    #print("pushing=", edge[0])
                    visited[edge[0]] = True
        visited[cur] = False
        
"""
for k in range(P):
    for i in range(P):
        for j in range(P):
            if i != j and connections[i][k] != 0 and connections[j][k] != 0 and (connections[i][j] == 0 or connections[i][j] > connections[i][k] + connections[j][k]):
                connections[i][j] = connections[i][k] + connections[j][k]
"""

for i in range(P):
    spfa(d, edges, i)

result = sys.maxsize
for i in range(P):
    totalLen = 0
    for pasture in pastures:
        totalLen += d[i][pasture]
    if result > totalLen:
        result = totalLen
        #print("i=", i)

with open('butter.out', 'w') as fout:
    fout.write(str(result) + '\n')