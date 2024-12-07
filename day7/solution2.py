import time
import itertools
file = open("day7/input.txt")

def findEquation(line):
    resultSplit = line.split(":")
    equationSplit = resultSplit[1].split()
    result = [resultSplit[0]]
    result.extend(equationSplit)
    result = list(map(int, result))
    return result

def operatorPerms(operators, permSpots):
    permutations = list(itertools.product(operators, repeat=permSpots))
    return permutations

def concatenate(a,b):
    return int(str(a) + str(b))

def createEquation(remaining, permutation):
    result = remaining[0]
    for i in range(len(permutation)):
        op = permutation[i]
        if op == "+":
            result += remaining[i+1]
        elif op == "*":
            result *= remaining[i+1]
        elif op == "||":
            result = concatenate(result, remaining[i+1])
    return result

def equationChecker(equation):
    goal = equation[0]
    remaining = equation[1:]
    permSpots = len(remaining) - 1
    operators = ["+", "*", "||"]
    operatorPermutations = operatorPerms(operators, permSpots)
    for permutation in operatorPermutations:
        if goal == createEquation(remaining, permutation):
            return goal
    return 0

def findTotal(file):
    total = 0
    lines = file.readlines()
    for line in lines:
        print(f"checking line {lines.index(line) + 1} of {len(lines)}", )
        total += equationChecker(findEquation(line))
    return total

startTime = time.time()
print("total: ", findTotal(file))
endTime = time.time()
print(f"time taken: {round(endTime-startTime, 3)} seconds")