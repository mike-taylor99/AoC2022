pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 9/input.txt'

SAME_ROW = [(0, y) for y in range(-1, 2)]
SAME_COLUMN = [(x, 0) for x in range(-1, 2)]
DIAGONALS = [(x, y) for x in range(-1, 2, 2) for y in range(-1, 2, 2)]
ALLOWED_DISTANCES = set(SAME_ROW + SAME_COLUMN + DIAGONALS)

def isTailCloseEnough(head, tail):
    distance = (head[0] - tail[0], head[1] - tail[1])
    return distance in ALLOWED_DISTANCES

def closestDistance(head, tail):
    row_dist, col_dist = head[0] - tail[0], head[1] - tail[1]

    if isTailCloseEnough(head, tail):
        return tail
    elif row_dist == 0:
        for x, y in SAME_ROW:
            updatedTail = (tail[0] + x, tail[1] + y)
            if isTailCloseEnough(head, updatedTail):
                return updatedTail
    elif col_dist == 0:
        for x, y in SAME_COLUMN:
            updatedTail = (tail[0] + x, tail[1] + y)
            if isTailCloseEnough(head, updatedTail):
                return updatedTail
    else:
        for x, y in DIAGONALS:
            updatedTail = (tail[0] + x, tail[1] + y)
            if isTailCloseEnough(head, updatedTail):
                return updatedTail

def applyMove(head, tail, move):
    direction, amount = move
    retHead, retTail = head, tail
    tailVisited = [tail]

    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    x, y = directions[direction]

    for i in range(amount):
        retHead = (retHead[0] + x, retHead[1] + y)
        retTail = closestDistance(retHead, retTail)
        tailVisited.append(retTail)
    
    return retHead, retTail, tailVisited

def simulateRope(moves):
    head = tail = (0, 0)
    tailVisits = [tail]

    for move in moves:
        head, tail, visits = applyMove(head, tail, move)
        tailVisits += visits

    return tailVisits

def trackExtraKnots(firstTailMotions, numExtraRopes):
    motions = firstTailMotions

    for i in range(numExtraRopes):
        currTail = (0, 0)
        tailVisits = [currTail]
        
        for move in motions:
            currTail = closestDistance(move, currTail)
            tailVisits.append(currTail)
        
        motions = tailVisits

    return motions
    
with open(pathname) as input:
    motions = [line.strip().split(' ') for line in input]
    motions = [(x, int(y)) for x, y in motions]

    firstTailMotions = simulateRope(motions)
    tenthKnotMotions = trackExtraKnots(firstTailMotions, 8)

    print(f'How many positions does the tail of the rope visit at least once? {len(set(firstTailMotions))}')
    print(f'How many positions does the tail of the rope visit at least once? {len(set(tenthKnotMotions))}')
