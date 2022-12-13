import numpy

pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 8/input.txt'

def inspectRow(map, row, column):
    maxLeft = max(map[row][:column])
    maxRight = max(map[row][column+1:])

    isVisibleLeft = maxLeft < map[row][column]
    isVisibleRight = maxRight < map[row][column]

    return isVisibleLeft or isVisibleRight

def inspectColumn(map, row, column):
    transposeMap = numpy.transpose(map)

    return inspectRow(transposeMap, column, row)

def scenicScoreRight(rightTrees, height):
    views = [height > tree for tree in rightTrees]
    if False in views:
        return views.index(False) + 1
    return len(views)

def scenicScoreLeft(leftTrees, height):
    return scenicScoreRight(leftTrees[::-1], height)

def inspectRowScenicScore(map, row, column):
    leftScore = scenicScoreLeft(map[row][:column], map[row][column])
    rightScore = scenicScoreRight(map[row][column+1:], map[row][column])

    transposeMap = numpy.transpose(map)
    upScore = scenicScoreLeft(transposeMap[column][:row], transposeMap[column][row])
    downScore = scenicScoreRight(transposeMap[column][row+1:], transposeMap[column][row])

    return leftScore * rightScore * upScore * downScore
    
with open(pathname) as input:
    lines = [[int(char) for char in line.strip()] for line in input]

    totalVisibleOutside = (len(lines) * 2) + ((len(lines[0]) - 2) * 2)
    bestScenicScore = 0

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[1]) - 1):
            totalVisibleOutside += inspectRow(lines, i, j) or inspectColumn(lines, i, j)

    for i in range(1, len(lines)):
        for j in range(1, len(lines[1])):
            bestScenicScore = max(bestScenicScore, inspectRowScenicScore(lines, i, j))
            
    print(f'How many trees are visible from outside the grid? {totalVisibleOutside}')
    print(f'What is the highest scenic score possible for any tree? {bestScenicScore}')
