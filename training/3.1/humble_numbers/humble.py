"""
PROG: humble
LANG: PYTHON3

"""
import sys
with open('humble.in', 'r') as fin:
  lines = fin.readlines()

K, N = map(int, lines[0].split())

primes = list(map(int, lines[1].split()))  

#print(K, N)
#print(primes)

indexes = [0] * K

results = [0] * (N+1)
results[0] = 1

for i in range(1, N+1):
    minNext = sys.maxsize
    m = 0
    for j in range(K):
        while results[indexes[j]] * primes[j] <= results[i-1]:
            indexes[j] += 1
        curVal = results[indexes[j]] * primes[j]
        if minNext > curVal:
            minNext = curVal
            m = j
            if minNext == results[i-1] + 1:
                break
    results[i] = minNext
    indexes[m] += 1

with open('humble.out', 'w') as fout:
    fout.write(str(results[N]) + '\n')