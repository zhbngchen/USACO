fin = open('traffic.in', 'r')
fout = open('traffic.out', 'w')

N = int(fin.readline())
lines = []
for _ in range(N):
    lines.append(fin.readline().strip())
print(lines)

def processDn(a, b, sign, num1, num2):
    if sign == 'on':
        a += num1
        b += num2
    elif sign == 'off':
        a -= num2
        b -= num1
    else:
        a = max(a, num1)
        b = min(b, num2)
    return a, b

def processUp(a, b, sign, num1, num2):
    if sign == 'on':
        a -= num2
        b -= num1
    elif sign == 'off':
        a += num1
        b += num2
    else:
        a = max(a, num1)
        b = min(b, num2)
    return a, b

end1 = 0
end2 = 0
for i in range(N):
    sign, str1, str2 = lines[i].split()
    num1 = int(str1)
    num2 = int(str2)
    if end1 == 0 and end2 == 0:
        if sign == 'none':
            end1 = num1
            end2 = num2
    else:
        end1, end2 = processDn(end1, end2, sign, num1, num2)

start1 = 0
start2 = 0
for i in range(N-1, -1, -1):
    sign, str1, str2 = lines[i].split()
    num1 = int(str1)
    num2 = int(str2)
    if start1 == 0 and start2 == 0:
        if sign == 'none':
            start1 = num1
            start2 = num2
    else:
        start1, start2 = processUp(start1, start2, sign, num1, num2)

if start1 < 0:
    start1 = 0
if start2 < 0:
    start2 = 0
if end1 < 0:
    end1 = 0
if end2 < 0:
    end2 = 0

fout.write(str(start1) + ' ' + str(start2) + '\n')
fout.write(str(end1) + ' ' + str(end2) + '\n')
fout.close()