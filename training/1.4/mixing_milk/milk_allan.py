'''
LANG: PYTHON3
PROG: milk
'''

fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

full = fin.read()
print(full)
full = full.split('\n')
full[0] = full[0].split()
milkneeded = int(full[0][0])

cost = 0
full.pop(0)
dupelist = full
for term in dupelist:
    term = term.split()
dupelist.sort()
print(dupelist)
while milkneeded > 0:
    milkprice = int(dupelist[0][0])
    milkquant = int(dupelist[0][2:])
    if milkneeded >= milkquant:
        milkneeded -= milkquant
        print(cost,milkprice,milkquant)
        cost += (milkprice*milkquant)
        dupelist.pop(0)
    if milkquant > milkneeded:
        cost += (milkprice*milkneeded)
        milkneeded = 0
fout.write(str(cost) + '\n')