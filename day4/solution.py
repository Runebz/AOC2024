import re

file = open("day4\input.txt", "r")
total = 0

def checkHorizontal(txt):
    instances = re.findall("XMAS", txt)
    instances.extend(re.findall("SAMX", txt))
    return len(instances)

def checkVertical(line, vertOffset):
    vertCount = 0
    for i in range(len(line)):
        if line[i] == "X":
            try:
                if lines[vertOffset-1][i] == "M" and lines[vertOffset-2][i] == "A" and lines[vertOffset-3][i] == "S":
                    vertCount += 1
            except IndexError:
                pass
            try:
                if lines[vertOffset+1][i] == "M" and lines[vertOffset+2][i] == "A" and lines[vertOffset+3][i] == "S": 
                    vertCount += 1
            except IndexError:
                pass
    return vertCount

def checkDiagonals(line, vertOffset):
    diagCount = 0
    for i in range(len(line)):
        if line[i] == "X":
            try:
                if lines[vertOffset-1][i-1] == "M" and lines[vertOffset-2][i-2] == "A" and lines[vertOffset-3][i-3] == "S":
                    diagCount += 1
            except IndexError:
                pass
            try:
                if lines[vertOffset+1][i-1] == "M" and lines[vertOffset+2][i-2] == "A" and lines[vertOffset+3][i-3] == "S": 
                    diagCount += 1
            except IndexError:
                pass
            try:
                if lines[vertOffset-1][i+1] == "M" and lines[vertOffset-2][i+2] == "A" and lines[vertOffset-3][i+3] == "S":
                    diagCount += 1
            except IndexError:
                pass
            try:
                if lines[vertOffset+1][i+1] == "M" and lines[vertOffset+2][i+2] == "A" and lines[vertOffset+3][i+3] == "S": 
                    diagCount += 1
            except IndexError:
                pass
    return diagCount

        

lines = file.readlines()

for i in range(len(lines)):
    total += checkHorizontal(lines[i]) + checkVertical(lines[i], i) + checkDiagonals(lines[i], i)

print(total)