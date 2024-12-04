import time
file = open("day 1\input.txt", "r")
leftList = []
rightList = []
diffs = []
total = 0

for line in file.readlines():
    split = line.split()
    leftList.append(split[0])
    rightList.append(split[1])
leftList.sort()
rightList.sort()
startTime = time.time_ns()
for i in range(0, len(leftList)):
    total += abs(int(leftList[i]) - int(rightList[i]))

endTime = time.time_ns()
print("sum of diffs: ", total)
print("time taken: ", str((endTime - startTime)/1000000))


