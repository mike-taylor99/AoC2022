pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 3/input.txt'

def listCharacters(line):
    characters = list(line)
    if '\n' in characters:
        characters.remove('\n')
    return characters

def convertCharacters(characters):
    return [ord(char) - 96 if char > 'Z' else ord(char) - 38 for char in characters]
    
with open(pathname) as input:
    sumOfPriorities, sumOfPriorities2 = 0, 0
    
    for line in input:
        characters = listCharacters(line)
        items = [ord(char) - 96 if char > 'Z' else ord(char) - 38 for char in characters]

        indexOfHalf = len(items) // 2

        firstCompartment = items[:indexOfHalf]
        secondCompartment = items[indexOfHalf:]

        priority = list(set(firstCompartment).intersection(set(secondCompartment)))[0]

        sumOfPriorities += priority

    print(f'The sum of priorities: {sumOfPriorities}')

    print('\n--- Part Two ---\n')

    input.seek(0)

    lines = [line for line in input]

    while(len(lines) > 0):
        group, lines = lines[:3], lines[3:]

        groupCharacters = [listCharacters(line) for line in group]
        groupItems = [convertCharacters(characters) for characters in groupCharacters]

        badgeItem = list(set(groupItems[0]).intersection(set(groupItems[1]), set(groupItems[2])))[0]
        
        sumOfPriorities2 += badgeItem

    print(f'The sum of priorities: {sumOfPriorities2}')
