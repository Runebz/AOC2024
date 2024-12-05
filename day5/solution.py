file = open("day5\input.txt", "r")
rules = []
lists = []
correctLists = []
total = 0

for line in file.readlines():
    if line.find("|") != -1:
        rules.append(list(map(int, line.strip("\n").split("|"))))
    if line.find(",") != -1:
        lists.append(list(map(int, line.split(","))))

for list in lists:
    invalid = False
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if [list[j], list[i]] in rules:
                invalid = True
                break
        if invalid:
            break
    if not invalid:
        correctLists.append(list)

for list in correctLists:
    middle = round((len(list) - 1) / 2)
    total += list[middle]

print(total)
