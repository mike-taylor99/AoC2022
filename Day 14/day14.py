import numpy as np

pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 14/input.txt'

def parseLines(lines):
    paths = [line.split(' -> ') for line in lines]
    paths = [[pair.split(',') for pair in line] for line in paths]
    paths = [[[int(val) for val in pair] for pair in path] for path in paths]
    paths = [[tuple(pair) for pair in path] for path in paths]
    return paths

def getMapBounds(paths):
    minX = minY = float('inf')
    maxX = maxY = 0
    
    for path in paths:
        for x, y in path:
            if y < minY:
                minY = y
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y

    return minX, minY, maxX, maxY

def insertIntoMap(item, coord, map, bounds):
    x, y = coord
    minX, minY, maxX, maxY = bounds

    newY, newX = y, x - minX
    map[newY][newX] = item

def drawRock(coord1, coord2, map, bounds):
    x1, y1 = coord1
    x2, y2 = coord2

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            insertIntoMap('#', (x1, y), map, bounds)
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            insertIntoMap('#', (x, y1), map, bounds)

def findBottom(source, map, bounds):
    x_prev, y = source
    minX, minY, maxX, maxY = bounds
    x = x_prev - minX

    for yi in range(y+1, maxY + 1):
        if map[yi][x] != '.':
            return (x_prev, yi - 1), map[yi][x] == 'o'

def dropSand(source, map, bounds, cameDiagonally = False):
    vals = findBottom(source, map, bounds)
    minX, minY, maxX, maxY = bounds

    if not vals:
        return False

    drop, onSand = vals
    x, y = drop
    if onSand or cameDiagonally:
        isRightFree = x != maxX and y != maxY and map[y+1][x-minX+1] == '.'
        isLeftFree = x != minX and y != maxY and map[y+1][x-minX-1] == '.'

        if isLeftFree:
            return dropSand((x-1, y), map, bounds, True)
        elif isRightFree:
            return dropSand((x+1, y), map, bounds, True)

    if x == minX or x == maxX or y == maxY:
        return False
    
    map[y][x-minX] = 'o'
    return True

def generateMap(paths):
    bounds = getMapBounds(paths)
    minX, minY, maxX, maxY = bounds

    map = np.full((maxY + 1, maxX - minX + 1), '.')

    for path in paths:
        for i in range(len(path) - 1):
            drawRock(path[i], path[i+1], map, bounds)

    i = 0
    while map[0][500-minX] == '.':
        x = dropSand((500, 0), map, bounds)
        if not x:
            break
        i += 1
    
    return i

def generateMapPart2(paths):
    bounds = getMapBounds(paths)
    minX, minY, maxX, maxY = bounds

    length_X = maxX - minX
    startFloor, endFloor = minX - 3 * length_X, minX + 3 * length_X
    
    newPaths = paths + [[(startFloor, maxY + 2), (endFloor, maxY + 2)]]

    return generateMap(newPaths)

with open(pathname) as input:
    lines = [line.strip() for line in input]
    paths = parseLines(lines)

    print(f'How many units of sand come to rest before sand starts flowing into the abyss below? {generateMap(paths)}')
    print(f'How many units of sand come to rest? {generateMapPart2(paths)}')
