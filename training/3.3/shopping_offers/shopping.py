"""
PROG: shopping
LANG: PYTHON3

"""
import sys

with open("shopping.in", "r") as fin:
  lines = fin.readlines()

s = int(lines[0])
b = int(lines[s+1])

offersNumItemsCombo = [[0 for _ in range(6)] for _ in range(100)]
offersPrice = [0 for _ in range(100)]

indexes = {}
index = 0

buys = [0 for _ in range(6)]

for i in range(s):
  elements = list(map(int, lines[i+1].split()))
  num = elements[0]
  for j in range(num):
    itemCode = elements[2*j+1]
    numItems = elements[2*j+2]
    if itemCode not in indexes.keys():
      indexes[itemCode] = index
      index += 1
    offersNumItemsCombo[i][indexes[itemCode]] = numItems
  offersPrice[i] = elements[2*elements[0]+1]

for i in range(b):
  elements = list(map(int, lines[i+s+2].split()))
  itemCode = elements[0]
  numItems = elements[1]
  if itemCode not in indexes.keys():
    indexes[itemCode] = index
    index += 1
  offersNumItemsCombo[i+s][indexes[itemCode]] = 1
  offersPrice[i+s] = elements[2]
  buys[indexes[itemCode]] = numItems

dp = [[[[[sys.maxsize/2 for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)]
dp[0][0][0][0][0] = 0

for i in range(len(offersNumItemsCombo)):
  numItems0 = offersNumItemsCombo[i][0]
  numItems1 = offersNumItemsCombo[i][1]
  numItems2 = offersNumItemsCombo[i][2]
  numItems3 = offersNumItemsCombo[i][3]
  numItems4 = offersNumItemsCombo[i][4]
  for j in range(buys[4]+1):
    for k in range(buys[3]+1):
      for l in range(buys[2]+1):
        for m in range(buys[1]+1):
          for n in range(buys[0]+1):
            if j+numItems4 < 6 and k+numItems3 < 6 and l+numItems2 < 6 and m+numItems1 < 6 and n+numItems0 < 6 and dp[j+numItems4][k+numItems3][l+numItems2][m+numItems1][n+numItems0] > dp[j][k][l][m][n] + offersPrice[i]:
              dp[j+numItems4][k+numItems3][l+numItems2][m+numItems1][n+numItems0] = dp[j][k][l][m][n] + offersPrice[i]

with open('shopping.out', 'w') as fout:
  fout.write(str(dp[buys[4]][buys[3]][buys[2]][buys[1]][buys[0]]) + '\n')