"""
PROG: milk2
LANG: PYTHON3
"""

import sys

fin = open("milk2.in", "r")
fout = open ('milk2.out', 'w')

N = int(fin.readline())
schedules = []
for i in range(N):
  start, stop = map(int, fin.readline().split())
  schedules.append([start, stop])

schedules.sort()
prevStart = 0
prevStop = 0
longestMilking = 0
longestIdle = 0
for start, stop in schedules:
  if longestMilking == 0:
    longestMilking = stop - start
    prevStart = start
    prevStop = stop
  else:
    if start <= prevStop and stop >= prevStop:
      prevStop = stop
    elif start > prevStop:
      if longestMilking < prevStop - prevStart:
        longestMilking = prevStop - prevStart
      if longestIdle < start - prevStop:
        longestIdle = start - prevStop
      prevStart = start
      prevStop = stop

if longestMilking < prevStop - prevStart:
  longestMilking = prevStop - prevStart

fout.write(str(longestMilking) + ' ' + str(longestIdle) + '\n')
  
fout.close()
