"""
PROG: beads
LANG: PYTHON3
"""

class Bead:
    def __init__(self, c):
        self.color = c
        self.prev = None
        self.next = None

class Necklace:
    def __init__(self):
        self.head = None
    def addBeadToTail(self, c):
        b = Bead(c)
        if self.head == None:
            self.head = b
            b.next = b
            b.prev = b
        else:
            last = self.head.prev
            last.next = b
            b.prev = self.head.prev
            self.head.prev = b
            b.next = self.head

def buildNacklace(inStr):
    necklace = Necklace()
    for c in inStr:
        necklace.addBeadToTail(c)
    return necklace

def collectBeadsFromLeft(bead):
    start = bead
    resultNum = 1
    color = bead.color
    curBead = bead
    print("left color=", color)

    while True:
        curBead = curBead.prev
        print("color=", color, ", cur color=", curBead.color)
        if color == 'w':
            color = curBead.color
        elif curBead.color != 'w' and color != curBead.color or curBead == start:
            print("break")
            break
        resultNum += 1
        if resultNum >= N:
            return N
    print("left result=", resultNum)
    return resultNum


def collectBeadsFromright(bead):
    if bead.next == bead:
        return 0
    start = bead.next
    resultNum = 1
    color = start.color
    curBead = start
    print("right color=", color)
    while True:
        curBead = curBead.next
        print("color=", color, ", cur color=", curBead.color)
        if color == 'w':
            color = curBead.color
        elif curBead.color != 'w' and color != curBead.color or curBead == start:
            print("break")
            break
        resultNum += 1
        if resultNum >= N:
            return N
    print("right result=", resultNum)
    return resultNum

def collectBeads(bead):
    return collectBeadsFromLeft(bead) + collectBeadsFromright(bead)

#import sys

fin = open("beads.in", "r")
fout = open ('beads.out', 'w')

N = int(fin.readline())
inBeads = fin.readline().rstrip()

necklace = buildNacklace(inBeads)

maxNum = 1

curBead = necklace.head
count = 0
while True:
    count += 1
    print("count=", count)
    numBeads = collectBeads(curBead)
    if numBeads >= N:
        numBeads = N
    if numBeads > maxNum:
        maxNum = numBeads
    if curBead.next == necklace.head:
        break
    curBead = curBead.next

fout.write(str(maxNum) + '\n')
  
fout.close()