"""
PROG: ride
LANG: PYTHON3
"""

import sys

fin = open("ride.in", "r")
fout = open ('ride.out', 'w')

cometName = fin.readline().strip()
groupName = fin.readline().strip()

listComet = list(cometName)

productComet = 1
productGroup = 1

for c in cometName:
  productComet *= ord(c) - ord('A') + 1

for c in groupName:
  productGroup *= ord(c) - ord('A') + 1

result = ''
if (productComet % 47) == (productGroup % 47):
	result = 'GO'
else:
	result = 'STAY'

fout.write(result + '\n')

fout.close()

