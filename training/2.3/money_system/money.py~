"""
PROG: money
LANG: PYTHON3

"""
import sys
with open('money.in', 'r') as fin:
  lines = fin.readlines()

V, N = map(int, lines[0].split())
coins = list(map(int, lines[1].split()))
if len(coins) != V:
  i = 2
  while len(coins) < V:
    coins.append(int(lines[i]))
    i += 1

print(V, N)
print(coins)

####################### coins 1, 2, 5 case ###############################################
#  	0	1	2	3	4	5	6	7	8	9	10

# 0	0	0	0	0	0	0	0	0	0	0	0

# 1($1)	1	1	1	1	1	1	1	1	1	1	1

# 2($2)	1	1	2	2	3	3	4	4	5	5	6
											
# 3($5)	1	1	2	2	3	4	5	6	7	8	10 (10 is from above 6 and 4 (col 10 - 5)

###############################################################################################

####################### coins 1, 2, 3, 4, 5 case ###############################################
#  	0	1	2	3	4	5	6	7	8	9	10

# 0	0	0	0	0	0	0	0	0	0	0	0

# 1($1)	1	1	1	1	1	1	1	1	1	1	1

# 2($2)	1	1	2	2	3	3	4	4	5	5	6
											
# 3($3)	1	1	2	3	4	5	7	8	10	12	14 (14 is from above 6 and 8 (col 10 - 3))

# 4($4)	1	1	2	3	5	6	9	11	15	18	23

# 5($5)	1	1	2	3	5	7	10	13	18	23	30 (30 is from above 23 and 7 (col 10 - 4))

###############################################################################################

dp = []
for i in range(V+1):
  emptyList = [0] * (N+1)
  dp.append([i for i in emptyList])

print("len of dp: ", len(dp))
print("len of dp[0]: ", len(dp[0]))

for i in range(1, V+1):
  for j in range(0, N+1):
    if j == 0:
      dp[i][j] = 1
    elif (j - coins[i - 1]) < 0:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = dp[i-1][j] + dp[i][j - coins[i - 1]]
      
with open('money.out', 'w') as fout:
  fout.write(str(dp[V][N]) + '\n')


