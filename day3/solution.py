import re
file = open("day3\input.txt", "r")
result = 0

for line in file.readlines():  
    x = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    for op in x:
        nums = re.findall("\d{1,3},\d{1,3}", op)
        nums = list(map(int, nums[0].split(",")))
        result += nums[0] * nums[1]
print(result)