"""
PROG: prefix
LANG: PYTHON3

"""
import sys

with open("prefix.in", "r") as fin:
  lines = fin.readlines()

index = 0
setPrim = []
while True:
    strings = lines[index].strip().split()
    index += 1
    if strings[0] == '.':
        break
    for string in strings:
        setPrim.append(string)

print("setPrim= ", setPrim)

"""
A AB BA CA BBC
.
ABABACABAABC

dp:
index:  0   1   2   3   4   5   6   7   8   9   10  11  12
status: 1   1   1   1   1   1   0   1   1   1   1   1   0
     S:     A   B   A   B   A   C   A   B   A   A   B   C
At current position, check current letter or up to previous 10 letters
(include current letter) to be in given patterns, plus the position right
before the letter(s) has status 1.
"""
1 5 7 6 4 3 7 2 6 5 2 4 1
S = ''
while index < len(lines):
    S += lines[index].strip()
    index += 1
print("S= ", S)
print("len(S)= ", len(S))
statusS = [0] * (len(S) + 1)
statusS[0] = 1
for i in range(len(S)):
    for j in range(10):
        if i >= j and statusS[i - j] == 1 and S[(i - j):(i+1)] in setPrim:
            statusS[i+1] = 1
            break

index = len(S)
while statusS[index] == 0:
    index -= 1

print("index= ", index)
with open('prefix.out', 'w') as fout:
  fout.write(str(index) + '\n')

