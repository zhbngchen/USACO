"""
PROG: castle
LANG: PYTHON3

"""
import sys

with open("castle.in", "r") as fin:
  lines = fin.readlines()

M, N = map(int, lines[0].split())

blocks = []
for row in range(N):
  blocks.append(list(map(int, lines[row+1].split())))

#print("M=", M, " N=", N)
#print(blocks)

blockRooms = [x[:] for x in [[-1] * M] * N] # room number that a block belongs to, from 0 to certain number
#print("blockRooms=", blockRooms)

roomBlockCounts = [] # block count per room
def searchBlocks(row, col, blocks, curRoom, blockRooms, roomBlockCounts):
  #print("before row=", row, " col=", col, " blockRooms[row][col]=", blockRooms[row][col], " blockRooms=", blockRooms)
  if blockRooms[row][col] != -1:
    return
  rooms = blockRooms[row]
  rooms[col] = curRoom
  roomBlockCounts[curRoom] += 1
  #print("row=", row, " col=", col, " curRooms=", curRoom, " roomBlockCounts=", roomBlockCounts, " blockRooms=", blockRooms)
  bit = 1
  for i in range(4):
    nextRow = row
    nextCol = col
    if (blocks[row][col] & (bit << i)) == 0:
      if i == 0:
        #print("first")
        nextCol = col - 1
      elif i == 1:
        #print("second")
        nextRow = row - 1
      elif i == 2:
        #print("third")
        nextCol = col + 1
      else: # i == 3
        #print("fourth")
        nextRow = row + 1
      searchBlocks(nextRow, nextCol, blocks, curRoom, blockRooms, roomBlockCounts)

curRoom = -1 
for row in range(N):
  for col in range(M):
    if blockRooms[row][col] == -1:
      curRoom += 1
      roomBlockCounts.append(0)
    searchBlocks(row, col, blocks, curRoom, blockRooms, roomBlockCounts)

#print("blockRooms=", blockRooms)
#print("roomBlockCounts=", roomBlockCounts)

maxBlockCounts = 0
wallPositions = []
for row in range(N-1, -1, -1):
  for col in range(M):
    for dir in ['E', 'N']:
      nextRow = row
      nextCol = col
      if dir == 'E' and col < M-1:
        nextCol = col + 1
      elif row > 0:
        nextRow = row - 1
      else:
        continue
      curRoom = blockRooms[row][col]
      nextRoom = blockRooms[nextRow][nextCol]
      if curRoom != nextRoom:
        combinedBlockCounts = roomBlockCounts[curRoom] + roomBlockCounts[nextRoom]
        if maxBlockCounts < combinedBlockCounts:
          maxBlockCounts = combinedBlockCounts
          wallPositions = [[row+1, col+1, dir]]
        elif maxBlockCounts == combinedBlockCounts:
          wallPositions.append([row+1, col+1, dir])

#print("maxBlockCounts=", maxBlockCounts)
#print("wallPositions=", wallPositions)

# sort west to east
wallPositions.sort(key=lambda x: x[1])
# pick most west
wallPositions = [i for i in wallPositions if i[1] == wallPositions[0][1]]

# sort south to north
wallPositions.sort(key=lambda x: x[0], reverse=True)
# pick most south
wallPositions = [i for i in wallPositions if i[0] == wallPositions[0][0]]

if len(wallPositions) > 1:
  wallPositions.sort(key=lambda x: x[2], reverse=True)

wallPosition = wallPositions[0]

with open('castle.out', 'w') as fout:
  fout.write(str(len(roomBlockCounts)) + '\n')
  fout.write(str(max(roomBlockCounts)) + '\n')
  fout.write(str(maxBlockCounts) + '\n')
  fout.write(str(wallPosition[0]) + ' ' + str(wallPosition[1]) + ' ' + wallPosition[2] + '\n') 
