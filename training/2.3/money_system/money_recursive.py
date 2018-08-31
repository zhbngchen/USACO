"""
PROG: money
LANG: PYTHON3

"""
import sys

with open('money.in', 'r') as fin:
  lines = fin.readlines()

V, N = map(int, lines[0].split())
coins = list(map(int, lines[1].split()))

coins.sort(reverse=True)

#print(V, N)
#print(coins)

def solve(indexCoins, value, coins, combo):
  if value == 0:
    #print("add combo=", combo)
    return 1
  if indexCoins == len(coins):
    return 0
  result = 0
  countCoins = value // coins[indexCoins]
  value -= countCoins * coins[indexCoins]
  combo += [coins[indexCoins]] * countCoins
  #print("indexCoins=", indexCoins, " value=", value, " countCoins=", countCoins, " combo: ", combo)
  for i in range(countCoins + 1):
    result += solve(indexCoins + 1, value, coins, combo)
    if i != countCoins:
      combo.pop()
    value += coins[indexCoins]
  return result
 
combo = []

result = solve(0, N, coins, combo)

with open('money.out', 'w') as fout:
  fout.write(str(result) + '\n')

