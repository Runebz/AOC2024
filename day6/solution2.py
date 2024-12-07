file = open("day6/input.txt", "r")
loopCount = 0
def findGuard(lines):
    for j in range(len(lines)):
        line = lines[j]
        for i in range(len(line)):
            if line[i] in "^v<>":
                return (j, i, line[i])  # Return the guard's position and direction

def turn(pos, lab):
    if 0 < pos[0] < len(lab) - 1 and 0 < pos[1] < len(lab[0]) - 1:
        match pos[2]:
            case "^":
                if lab[pos[0] - 1][pos[1]] == "#":
                    return (pos[0], pos[1], ">")
            case "v":
                if lab[pos[0] + 1][pos[1]] == "#":
                    return (pos[0], pos[1], "<")
            case "<":
                if lab[pos[0]][pos[1] - 1] == "#":
                    return (pos[0], pos[1], "^")
            case ">":
                if lab[pos[0]][pos[1] + 1] == "#":
                    return (pos[0], pos[1], "v")
            case _:
                print("guard has no direction")
    return pos  # Return the original position if no turn is made

def walk(pos, lab):
    visited = set()
    uniqueVisited = set()
    outOfBounds = False
    # print("walking")
    while not outOfBounds:
        # print("Current pos:", pos)
        
        if pos == None or pos[0] < 0 or pos[0] >= len(lab) or pos[1] < 0 or pos[1] >= len(lab[0]):
            outOfBounds = True
            continue
        # Turn the guard if needed and update pos
        new_pos = turn(pos, lab)
        if new_pos != pos:  # If the position changes, log it
            # print("Turned to:", new_pos)
            pos = new_pos
            continue

        if detectLoop((pos[0], pos[1], pos[2]), visited):
            global loopCount
            loopCount += 1
            break
        # Move the guard
        
        
        if pos not in visited:
            visited.add(pos)
        if (pos[0], pos[1]) not in uniqueVisited:
            uniqueVisited.add((pos[0], pos[1]))
        # Update pos based on direction
        match pos[2]:
            case "^":
                pos = (pos[0] - 1, pos[1], pos[2])
            case "v":
                pos = (pos[0] + 1, pos[1], pos[2])
            case "<":
                pos = (pos[0], pos[1] - 1, pos[2])
            case ">":
                pos = (pos[0], pos[1] + 1, pos[2])
            case _:
                print("guard has no direction")
    return visited, uniqueVisited

def solve():
    lab = [line.strip("\n") for line in file.readlines()]
    print("Lab layout:")
    for row in lab:
        print(row)

    pos = findGuard(lab)
    print("Starting position:", pos)

    visited, uniqueVisited = walk(pos, lab)
    print("Visited positions:", len(uniqueVisited))
    return visited, uniqueVisited, pos

def detectLoop(pos, visited):
    if (pos[0], pos[1], pos[2]) in visited:
        return True
    return False


visited, uniqueVisited, startingPos = solve()

def createLabs():
    labs = []
    for pos in uniqueVisited:
        if pos == startingPos:
            continue
        file = open("day6/input.txt", "r")
        lab = [line.strip("\n") for line in file.readlines()]
        line = list(lab[pos[0]])
        line[pos[1]] = "#"
        lab[pos[0]] = ''.join(line)
        # print("placed '#' at ", coord)
        # print(lab[uniqueVisited[i][0]])
        file.close()
        labs.append(lab)
    return labs

labs = createLabs()

for lab in labs:
    walk(findGuard(lab), lab)
print("done. loops: ", loopCount)