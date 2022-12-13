pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 12/input.txt'

ALLOWED_MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def getMoves(point, x_bound, y_bound):
    x, y = point
    moves = []

    for move in ALLOWED_MOVES:
        x2, y2 = move
        if ((x + x2) < 0) or ((y + y2) < 0):
            continue
        elif ((x + x2) >= x_bound) or ((y + y2) >= y_bound):
            continue
        else:
            moves.append((x+x2, y+y2))

    return moves

def validMoves(point, map):
    currentChar = map[point[0]][point[1]]
    if currentChar == 'S':
        currentChar = 'a'
    elif currentChar == 'E':
        currentChar = 'z'
    currentElevation = ord(currentChar)
    
    moves = getMoves(point, len(map), len(map[0]))
    characters = [map[move[0]][move[1]] for move in moves]
    for i in range(len(characters)):
        if characters[i] == 'S':
            characters[i] = 'a'
        elif characters[i] == 'E':
            characters[i] = 'z'
    elevations = [ord(char) for char in characters]
    allowedMoves = [elevation - currentElevation < 2 for elevation in elevations]

    returnValues = []
    for i in range(len(allowedMoves)):
        if allowedMoves[i]:
            returnValues.append(moves[i])

    return returnValues

def performMoves(startPoint, map):
    points_visited = { startPoint }
    queue = []
    
    validStartMoves = validMoves(startPoint, map)
    for move in validStartMoves:
        queue.append({'point': move, 'numSteps': 1})
    
    while len(queue) > 0:
        next = queue[0]
        point = next['point']
        if point not in points_visited:
            moves = validMoves(point, map)
            for x, y in moves:
                if map[x][y] == 'E':
                    return next['numSteps'] + 1
                queue.append({'point': (x, y), 'numSteps': next['numSteps'] + 1})
        points_visited.add(point)
        queue = queue[1:]

def findStartPoint(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                return (i, j)

def findLowestElevations(map):
    points = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'a' or map[i][j] == 'S':
                points.append((i, j))
    return points

def partOneFewestSteps(map):
    startPoint = findStartPoint(map)
    return performMoves(startPoint, map)

def partTwoFewestSteps(map):
    fewestSteps = float('inf')
    startingPoints = findLowestElevations(map)

    for startPoint in startingPoints:
        numSteps = performMoves(startPoint, map)

        if numSteps and numSteps < fewestSteps:
            fewestSteps = numSteps

    return fewestSteps

with open(pathname) as input:
    lines = [line.strip() for line in input]
    map = [[char for char in line] for line in lines]

    print(f'What is the fewest steps required to move from your current position to the location that should get the best signal? {partOneFewestSteps(map)}')
    print(f'What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal? {partTwoFewestSteps(map)}')
