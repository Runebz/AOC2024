import time
file = open("day2\input.txt", "r")
safeCount = 0

def firstCheck(line):
    split = list(map(int, line.split()))
    temp = split.copy()
    for i in range(len(split)):
        temp.pop(i)
        if secondCheck(temp):
            return temp
        temp = split.copy()
    return []

def secondCheck(split):
    desc = False
    asc = False
    if split == []:
        return False
    for i in range(len(split) - 1):
        if split[i+1] - split[i] < 0:
            desc = True
        elif split[i+1] - split[i] > 0:
            asc = True
        if asc and desc:
            return False
        if abs(split[i+1] - split[i]) < 1 or abs(split[i+1] - split[i]) > 3:
            return False
    return True

startTime = time.time_ns()
for line in file.readlines():
    split = firstCheck(line)
    if secondCheck(split):
        safeCount += 1
endTime = time.time_ns()

print("no. of safe reports: ", safeCount)
print("time taken (in ms): ", (endTime - startTime)/1000000)

