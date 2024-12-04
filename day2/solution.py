import time
file = open("day2\input.txt", "r")
safeCount = 0

startTime = time.time_ns()
for line in file.readlines():
    split = list(map(int, line.split()))
    desc = False
    asc = False
    for i in range(len(split) - 1):
        if split[i+1] - split[i] < 0:
            desc = True
        elif split[i+1] - split[i] > 0:
            asc = True
        if desc and asc:
            break
        if abs(split[i+1] - split[i]) < 1 or abs(split[i+1] - split[i]) > 3:
            break
        elif i == len(split) - 2:
            safeCount += 1

endTime = time.time_ns()

print("no. of safe reports: ", safeCount)
print("time taken (in ms): ", (endTime - startTime)/1000000)

