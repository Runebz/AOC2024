file = open("day5\input.txt", "r")
rules = []
lists = []
incorrectLists = []
total = 0

def fixList(list):
    fixed = False
    toFix = list.copy()
    fixedList = []
    while not fixed:
        print(fixedList)
        index = 0
        for i in range(len(toFix)):
            inserted = False
            for j in range(len(fixedList)+1):
                temp = fixedList.copy()
                temp.insert(j, toFix[i])
                if checkList(temp):
                    fixedList.insert(j, toFix[i])
                    index = i
                    inserted = True
                    break
            if inserted:
                break
        toFix.pop(index)
        if len(fixedList) == len(list) and checkList(fixedList):
            fixed = True

    return fixedList

def checkList(list):
    invalid = False
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if [list[j], list[i]] in rules:
                invalid = True
                break
        if invalid:
            break
    if not invalid:
        return True

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
    if invalid:
        incorrectLists.append(list)

for list in incorrectLists:
    fixedList = fixList(list)
    middle = round((len(fixedList) - 1) / 2)
    total += fixedList[middle]

print(total)
