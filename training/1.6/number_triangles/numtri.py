"""
PROG: numtri
LANG: PYTHON3

"""
import sys

with open("numtri.in", "r") as fin:
  lines = fin.readlines()

rows = int(lines[0])
data = []
dp = []
for i in range(rows):
  data.append(list(map(int, lines[i+1].split())))
  dp2 = []
  if i == 0:
    dp2.append(data[0][0])
  elif i == 1:
    for j in range(i+1):
      dp2.append(dp[0] + data[i][j])
  else:
    for j in range(i+1):
      if j == 0:
        dp2.append(dp[0] + data[i][0])
      else:
        #print("i=", i, " j=", j, " dp=", dp, " data=", data)
        if j != i:
          dp2.append(max(dp[j-1], dp[j]) + data[i][j])
        else:
          dp2.append(dp[j-1] + data[i][j])
  dp = dp2
#print(dp)

with open('numtri.out', 'w') as fout:
  fout.write(str(max(dp)) + '\n')
