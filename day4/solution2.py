import re

file = open("day4\input.txt", "r")
total = 0
lines = file.readlines()
mList = []
mDict = {}

def find_m(vertOffset, line):
    for i in range(len(line)):
        if line[i] == "M":
            uncheckedDirections = [True, True, True, True] #up-right, up-left, down-right, down-left
            mDict.update({(vertOffset, i): uncheckedDirections})
            mList.append([vertOffset, i])

def checkUR(vertOffset, index):
    foundMatch = False
    if lines[vertOffset][index] == "M":
        if vertOffset > 1 and lines[vertOffset-1][index+1] == "A" and lines[vertOffset-2][index+2] == "S":
            foundMatch = True
        unchecked = mDict.get((vertOffset, index))
        #print(f"checkUR for {vertOffset}, {index}: {unchecked}",)
        unchecked[0] = False
        mDict.update({(vertOffset, index): unchecked})
    return foundMatch
    
def checkUL(vertOffset, index):
    foundMatch = False
    if lines[vertOffset][index] == "M":
        if vertOffset > 1 and lines[vertOffset-1][index-1] == "A" and lines[vertOffset-2][index-2] == "S":
            foundMatch = True
        unchecked = mDict.get((vertOffset, index))
        #print(f"checkUL for {vertOffset}, {index}: {unchecked}",)
        unchecked[1] = False
        mDict.update({(vertOffset, index): unchecked})
    return foundMatch
    
def checkDR(vertOffset, index):
    foundMatch = False
    if lines[vertOffset][index] == "M":
        if vertOffset < len(lines) - 2 and lines[vertOffset+1][index+1] == "A" and lines[vertOffset+2][index+2] == "S":
            foundMatch = True
        unchecked = mDict.get((vertOffset, index))
        #print(f"checkDR for {vertOffset}, {index}: {unchecked}",)
        unchecked[2] = False
        mDict.update({(vertOffset, index): unchecked})
    return foundMatch
    
def checkDL(vertOffset, index):
    foundMatch = False
    if lines[vertOffset][index] == "M":
        if vertOffset < len(lines) - 2 and lines[vertOffset+1][index-1] == "A" and lines[vertOffset+2][index-2] == "S":
            foundMatch = True
        unchecked = mDict.get((vertOffset, index))
        #print(f"checkDL for {vertOffset}, {index}: {unchecked}",)
        unchecked[3] = False
        mDict.update({(vertOffset, index): unchecked})
    return foundMatch
    
def checkDiagonals(vertOffset, index, unchecked):
    result = 0
    if unchecked[0]:
        if checkUR(vertOffset, index):
            if checkDR(vertOffset - 2, index) ^ checkUL(vertOffset, index + 2):
                result += 1
    if unchecked[1]:
        if checkUL(vertOffset, index):
            if checkDL(vertOffset - 2, index) ^ checkUR(vertOffset, index - 2):
                result += 1
    if unchecked[2]:
        if checkDR(vertOffset, index):
            if checkUR(vertOffset + 2, index) ^ checkDL(vertOffset, index + 2):
                result += 1
    if unchecked[3]:
        if checkDL(vertOffset, index):
            if checkUL(vertOffset + 2, index) ^ checkDR(vertOffset, index - 2):
                result += 1
    return result

def solve():
    for i in range(len(lines)):
        find_m(i, lines[i])
    for coord in mList:
        global total
        total += checkDiagonals(coord[0], coord[1], mDict.get((coord[0], coord[1])))

solve()
print(total)