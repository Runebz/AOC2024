import re
file = open("day3\input.txt", "r")
result = 0

lines = file.readlines()
txt = ''.join(line.strip("\n") for line in lines)

instructions = re.sub("don't\(\)(.*?)do\(\)", '', txt, flags=re.DOTALL)
instructions = instructions.split("don't()")
print(instructions)
mul_finder = re.compile("mul\(\d{1,3},\d{1,3}\)")
num_finder = re.compile("\d{1,3},\d{1,3}")

for op in re.findall(mul_finder, instructions[0]):
        nums = list(map(int, re.findall(num_finder, op)[0].split(",")))
        print(op)
        result += nums[0] * nums[1]

print(result)