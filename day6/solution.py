file = open("day6\input.txt")
lab = file.readlines()
visited = []

def findGuard(lines):
    for j in range(len(lines)):
        line = lines[j]
        for i in range(len(line)):
            if line[i] == "^":
                return [[j, i], line[i]]
            elif line[i] == "v":
                return [[j, i], line[i]]
            elif line[i] == "<":
                return [[j, i], line[i]]
            elif line[i] == ">":
                return [[j, i], line[i]]
            
pos = findGuard(lab)[0]
direction = findGuard(lab)[1]
print("starting pos: ", pos)
print("starting direction: ", direction)

def walk():
    global pos
    global direction
    outOfBounds = False
    while not outOfBounds:
        if pos[0] < 0 or pos[0] == len(lab) or pos[1] < 0 or pos[1] == len(lab[0]):
            outOfBounds = True
            continue
        if [pos[0], pos[1]] not in visited:
            visited.append([pos[0], pos[1]])
        match direction:
            case "^":
                pos[0] -= 1
            case "v":
                pos[0] += 1
            case "<":
                pos[1] -= 1
            case ">":
                pos[1] += 1
            case _:
                print("guard has no direction")
        turn() #turns the guard if needed
    
def turn():
    global pos
    global direction
    if pos[0] > 0 and pos[0] < len(lab) - 1:
        match direction:
            case "^":
                if lab[pos[0] - 1][pos[1]] == "#":
                    direction = ">"
            case "v":
                if lab[pos[0] + 1][pos[1]] == "#":
                    direction = "<"
            case "<":
                if lab[pos[0]][pos[1] - 1] == "#":
                    direction = "^"
            case ">":
                if lab[pos[0]][pos[1] + 1] == "#":
                    direction = "v"
            case _:
                print("guard has no direction")

def solve():
    walk()
    print(len(visited))
    file.close()
    return visited

solve()