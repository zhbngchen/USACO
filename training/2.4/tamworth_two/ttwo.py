"""
PROG: ttwo
LANG: PYTHON3
"""
import sys

with open('ttwo.in', 'r') as fin:
  lines = fin.readlines()

grid = []

for line in lines:
  grid.append(line.strip())

def locate(grid, person):
  for row, rowContent in enumerate(grid):
    for col, item in enumerate(rowContent):
      if item == person:
        return row, col

def nextDir(direction):
  if direction == 'N':
    return 'E'
  elif direction == 'E':
    return 'S'
  elif direction == 'S':
    return 'W'
  else:
    return 'N'

def move(grid, row, col, direction):
  newRow = row
  newCol = col
  newDirection = direction
  if direction == 'N':
    if row == 0 or grid[row-1][col] == '*':
      newDirection = nextDir(direction)
    else:
      newRow -= 1
  elif direction == 'E':
    if col == (len(grid) - 1) or grid[row][col+1] == '*':
      newDirection = nextDir(direction)
    else:
      newCol += 1
  elif direction == 'S':
    if row == (len(grid) - 1) or grid[row+1][col] == '*':
      newDirection = nextDir(direction)
    else:
      newRow += 1
  else: #direction == 'W'
    if col == 0 or grid[row][col-1] == '*':
      newDirection = nextDir(direction)
    else:
      newCol -= 1
  return newRow, newCol, newDirection

farmerRow, farmerCol = locate(grid, 'F')
farmerDir = 'N'
cowRow, cowCol = locate(grid, 'C')
cowDir = 'N'
setPositions = set()
tuplePosition = (farmerRow, farmerCol, farmerDir, cowRow, cowCol, cowDir)
steps = 0
while (tuplePosition not in setPositions and (farmerRow != cowRow or farmerCol != cowCol)):
  #print("tuplePosition = ", tuplePosition)
  #print("steps = ", steps)
  setPositions.add(tuplePosition)
  farmerRow, farmerCol, farmerDir = move(grid, farmerRow, farmerCol, farmerDir)
  cowRow, cowCol, cowDir = move(grid, cowRow, cowCol, cowDir)
  tuplePosition = (farmerRow, farmerCol, farmerDir, cowRow, cowCol, cowDir)
  steps += 1

#print("after tuplePosition = ", tuplePosition)

with open('ttwo.out', 'w') as fout:
  if farmerRow == cowRow and farmerCol == cowCol:
    fout.write(str(steps) + '\n')
  else:
    fout.write('0\n')
