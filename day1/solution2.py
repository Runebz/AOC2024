import time
file = open("day1\input.txt", "r")
leftList = []
rightList = []
diffs = []
total = 0
rightOffset = 0

for line in file.readlines():
    split = line.split()
    leftList.append(int(split[0]))
    rightList.append(int(split[1]))
leftList.sort()
rightList.sort()

startTime = time.time_ns()
for i in range(0, len(leftList)):
    numCount = 0
    for j in range(rightOffset, len(rightList)):
        if rightList[j] > leftList[i]:
            break
        if leftList[i] == rightList[j]:
            numCount += 1
        if rightList[j] < leftList[i]:
            rightOffset = j
    total += leftList[i] * numCount
endTime = time.time_ns()
print("similarity score: ", total)
print("time taken: ", str((endTime - startTime)/1000000))


