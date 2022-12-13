filepath = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 2/input.txt'

pointsMap = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6
        },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
        },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
        }
    }

pointsMapForPartTwo = {
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
        },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
        },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
        }
    }

with open(filepath) as input:
    totalScore = 0
    totalScore2 = 0
    
    for line in input:
        round = line.split(' ')
        round[-1] = round[-1].replace("\n", "")

        pointsOfShape = ord(round[-1]) - 87
        outcomeOfRound = pointsMap[round[-1]][round[0]]
        roundScore = pointsOfShape + outcomeOfRound

        totalScore += roundScore

    print(f'Total Score: {totalScore}')

    print('\n--- Part Two ---\n')

    input.seek(0)

    for line in input:
        round = line.split(' ')
        round[-1] = round[-1].replace("\n", "")

        moveToMake = pointsMapForPartTwo[round[-1]][round[0]]

        pointsOfShape = ord(moveToMake) - 87
        outcomeOfRound = pointsMap[moveToMake][round[0]]
        roundScore = pointsOfShape + outcomeOfRound

        totalScore2 += roundScore

    print(f'Total Score: {totalScore2}')
