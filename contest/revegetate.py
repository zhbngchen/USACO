fin = open("revegetate.in", 'r')
fout = open('revegetate.out', 'w')

N, M = map(int, fin.readline().split())
data = []
for _ in range(N+1):
    data.append([])
for _ in range(M):
    a, b = map(int, fin.readline().split())
    data[a].append(b)
    data[b].append(a)

print(data)
result = [0]*(N+1)
print(result)
for i in range(1, N+1):
    tmpResults = []
    for j in data[i]:
        if result[j] != 0:
            tmpResults.append(result[j])
    for j in range(1, N+1):
        if j not in tmpResults:
            result[i] = j
            break
    print("i=",i, "result=", result)
for r in result:
    if r != 0:
        fout.write(str(r))
fout.write('\n')
fout.close