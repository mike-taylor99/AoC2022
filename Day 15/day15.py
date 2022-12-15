import numpy as np

pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 15/input.txt'

def parseLine(line):
    removePortions = [
            'Sensor at ',
            ': closest beacon is at',
            ','
        ]

    parsed = line
    for portion in removePortions:
        parsed = parsed.replace(portion, '')
    parsed = parsed.split(' ')

    parsed = [(int(parsed[0].replace('x=', '')), int(parsed[1].replace('y=', ''))),
              (int(parsed[2].replace('x=', '')), int(parsed[3].replace('y=', '')))]
    
    return parsed
    
def parseLines(lines):
    parsedLines = []
    for line in lines:
        parsedLines.append(parseLine(line))
    return parsedLines

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def getBoundary(point, radius):
    x, y = point
    curr = (x, y + radius)

    while curr != (x + radius, y):
        curr = (curr[0] + 1, curr[1] - 1)
        yield curr
    while curr != (x, y - radius):
        curr = (curr[0] - 1, curr[1] - 1)
        yield curr
    while curr != (x - radius, y):
        curr = (curr[0] - 1, curr[1] + 1)
        yield curr
    while curr != (x, y + radius):
        curr = (curr[0] + 1, curr[1] + 1)
        yield curr
        
def partOne(parsed):
    Y=2000000
    radiusGroups = []
    for signal, beacon in parsed:        
        radius = manhattan(signal, beacon)
        distance = abs(signal[1] - Y)

        if radius < distance:
            continue
        radiusGroups.append((signal[0]-(radius-distance), signal[0]+(radius-distance)))

    N=int(5e7)
    O=int(1e6)

    result = [0 for i in range(N)]
    for lower, upper in radiusGroups:
        for i in range(lower + O, upper + O + 1):
            result[i] = 1

    for signal, beacon in parsed:
        if beacon[1] == Y:
            result[beacon[0] + O] = 0

    return sum(result)

def partTwo(parsed):
    M = N = 4000000
    for signal, beacon in parsed:
        radius = manhattan(signal, beacon)
        
        #check outer boundary
        for x_i, y_i in getBoundary(signal, radius + 1):
            if 0 <= x_i <= M and 0 <= y_i <= N:
                for comp_signal, comp_beacon in parsed:
                    if signal == comp_signal:
                        break
                    
                    comp_radius = manhattan(comp_signal, comp_beacon)
                    comp_signals = manhattan(signal, comp_signal)
                    
                    if comp_signals <= comp_radius:
                        break
                else:
                    return (4000000 * x_i) + y_i

with open(pathname) as input:
    lines = [line.strip() for line in input]
    parsed = parseLines(lines)
    print(f'In the row where y=2000000, how many positions cannot contain a beacon? {partOne(parsed)}')
    print(f'What is its tuning frequency? {partTwo(parsed)}')
