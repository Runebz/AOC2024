import re
import math
file = open("day7/input.txt")

def findEquation(line):
    resultSplit = line.split(":")
    equationSplit = resultSplit[1].split()
    result = [resultSplit[0]]
    result.extend(equationSplit)
    result = list(map(int, result))
    return result

def createEquation(remaining, perm):
    result = remaining[0]
    binRep = list(bin(perm)[2:])
    skipStep = False
    while len(binRep) < len(remaining) - 1:
        binRep.insert(0, "0")
    for i in range(1, len(remaining)):
        if binRep[i-1] == "0":
            result += remaining[i]
        elif binRep[i-1] == "1":
            result *= remaining[i]
    return result

def equationChecker(equation):
    goal = equation[0]
    remaining = equation[1:]
    permutations = int(math.pow(2,(len(remaining) - 1)))
    for i in range(permutations):
        if goal == createEquation(remaining, i):
            return goal
    return 0

def findTotal(file):
    total = 0
    for line in file.readlines():
        total += equationChecker(findEquation(line))
    return total

# print("total: ", equationChecker(findEquation("292: 11 6 16 20")))
print("total: ", findTotal(file))
