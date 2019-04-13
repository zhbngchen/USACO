fin = open("herding.in", 'r')
fout = open("herding.out", 'w')
a, b, c = map(int, fin.readline().split())

distAB = b - a
distBC = c - b
if distAB == 1 and distBC ==1:
    best = 0
    worst = 0
else:
    if distAB == 2 or distBC == 2:
        best = 1
    else:
        best = 2
    if distAB < distBC:
        maxDist = distBC
    else:
        maxDist = distAB
    worst = maxDist - 1
fout.write(str(best) + '\n')
fout.write(str(worst) + '\n')
fout.close()
