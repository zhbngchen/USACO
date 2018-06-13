"""
PROG: friday
LANG: PYTHON3
"""

import sys

fin = open("friday.in", "r")
fout = open ('friday.out', 'w')

N = int(fin.readline())

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#starting day is Jan. 13, 1900 and it is a Saturady
counts = [0, 0, 0, 0, 0, 0, 0] # Sat, Sun, Mon, Tue, Wed, Thu, Fri
days = 0
for year in range(N):
  for month in MONTHS:
    days = days % 7
    counts[days] += 1
    if month == 'Feb':
      if year % 4 != 0 or year == 0 or year == 200 or year == 300:
        days += 28
      else:
        days += 29
    elif month == 'Apr' or month == 'Jun' or month == 'Sep' or month == 'Nov':
      days += 30
    else:
      days += 31

for i in range(len(counts)):
  fout.write(str(counts[i]))
  if i != len(counts) - 1:
    fout.write(' ')

fout.write('\n')
  
fout.close()
