"""
PROG: maze1
LANG: PYTHON3
"""
import sys
import queue

with open('maze1.in', 'r') as fin:
  lines = fin.readlines()

W, H = map(int, lines[0].split())

# row    lines=2*row+2
# 0      2 
# 1      4
# 2      6

# col    lines=2*row+1
# 0      1
# 1      3
# 2      5

maze = []
exits = []
directions = ['N', 'E', 'S', 'W']
boundaries = ['-', '|', '-', '|']

# get the index of boundary with direction in original input 2-D array, 
# with current location (row and col), moving direction, and size of rows and columns,
# output boundary location and if the new location is an outside boundary of fences
def getIndexFromInput(row, col, direction, numRows, numCols):
  newRow = 2*row+2
  newCol = 2*col+1
  externalBoundary = False
  if direction == 'N':
    newRow -= 1
    if row == 0:
      externalBoundary = True
  elif direction == 'E':
    newCol += 1
    if col == numCols-1:
      externalBoundary = True
  elif direction == 'S':
    newRow += 1
    if row == numRows-1:
      externalBoundary = True
  else: #direction == 'W'
    newCol -= 1
    if col == 0:
      externalBoundary = True
  return newRow, newCol, externalBoundary

def getIndexNextMove(row, col, direction):
  newRow = row
  newCol = col
  if direction == 'N':
    newRow -= 1
  elif direction == 'E':
    newCol += 1
  elif direction == 'S':
    newRow += 1
  else: #direction == 'W'
    newCol -= 1
  return newRow, newCol

# Convert the original input to a 2-D list of H (row) and W (col)
# Each element in the 2-D list is a list of directions with which the next moves can be
for row in range(H):
  rowContent = []
  for col in range(W):
    itemContent = []
    for i, direction in enumerate(directions):
      boundaryRow, boundaryCol, externalBoundary = getIndexFromInput(row, col, direction, H, W)
      if lines[boundaryRow][boundaryCol] != boundaries[i]:
        if externalBoundary == True:
          exits.append([row, col])
        else:
          itemContent.append(direction)
    rowContent.append(itemContent)
  maze.append(rowContent)

def printArray(a):
  for i in a:
    print(i)

#print("maze:")
#printArray(maze)

#print("exits:", exits)

# Use BFS method (with queue implementation)
# From each exit, go to all adjacent connecting locations one by one,
# then go to the adjacent of each ones if either it was never entered or
# the step counts in the adjacent is larger than current count.
steps = [[0]*W for _ in range(H)]
q = queue.Queue(3800)
for exit in exits:
  q.put(exit)
  row = exit[0]
  col = exit[1]
  steps[row][col] = 1
  while not q.empty():
    cur = q.get()
    row = cur[0]
    col = cur[1]
    stepCount = steps[row][col] + 1
    directions = maze[row][col]
    for direction in directions:
      newRow, newCol = getIndexNextMove(row, col, direction)
      if steps[newRow][newCol] == 0 or steps[newRow][newCol] > stepCount:
        steps[newRow][newCol] = stepCount
        q.put([newRow, newCol])
  #print("steps:")
  #printArray(steps)  

result = 0
for row in steps:
  maxStep = max(row)
  if result < maxStep:
    result = maxStep

with open('maze1.out', 'w') as fout:
  fout.write(str(result) + '\n')
