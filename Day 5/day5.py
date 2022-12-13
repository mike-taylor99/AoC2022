pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 5/input.txt'

def createStacks(cratesRawInput, numStacks):
    stacks = [[] for i in range(numStacks)]
    for line in cratesRawInput:
        crates = [line[i:i+4] for i in range(0, len(line), 4)]
        for i in range(len(crates)):
            if ' ' in crates[i]:
                crates[i] = crates[i].replace(' ', '')
            if '[' in crates[i]:
                crates[i] = crates[i].replace('[', '').replace(']', '')
            if '\n' in crates[i]:
                crates[i] = crates[i].replace('\n', '')

            if crates[i] != '':
                stacks[i].append(crates[i])
    return stacks

def parseMoves(movesRawInput):
    parsedMoves = []
    for line in movesRawInput:
        removeMove = line.replace('move ', '')
        findSpaceIndex = removeMove.find(' ')

        move = int(removeMove[:findSpaceIndex])

        removeFrom = removeMove[findSpaceIndex+1:].replace('from ', '')
        findSpaceIndex = removeFrom.find(' ')

        frm = int(removeFrom[:findSpaceIndex])

        removeTo  = removeFrom[findSpaceIndex+1:].replace('to ', '')
        findNewLine = removeTo.find('\n')

        if findNewLine == -1:
            to = int(removeTo)
        else:
            to = int(removeTo[:findNewLine])

        parsedMoves.append((move, frm, to))
    return parsedMoves

def applyMove(move, stacks, isCrateMover9001):
    numCrates, frm, to = move
    frm, to = frm-1, to-1

    crates = stacks[frm][:numCrates]

    if(not isCrateMover9001):
        crates = crates[::-1]

    stacks[frm] = stacks[frm][numCrates:]
    stacks[to] = crates + stacks[to]

def applyMoves(moves, stacks, isCrateMover9001):
    for move in moves:
        applyMove(move, stacks, isCrateMover9001)

def topCrates(moves, stacks, isCrateMover9001):
    finalString = ''
    
    applyMoves(moves, stacks, isCrateMover9001)

    for stack in stacks:
        finalString += stack[0]

    return finalString

with open(pathname) as input:
    numStacks = 0
    cratesRaw, movesRaw = [], []
    lines = [line for line in input]

    passedRawCrates = False
    
    for line in lines:
        if line.startswith(' 1'):
            removeNewLine = line.replace('\n', '')
            removeNewLine = removeNewLine.strip()
            removeNewLine = removeNewLine[::-1]
            
            indexOfSpace = removeNewLine.find(' ')
            
            numStacks = int(removeNewLine[:indexOfSpace])
            continue
        elif line == '\n':
            passedRawCrates = True
            continue

        if passedRawCrates:
            movesRaw.append(line)
        else:
            cratesRaw.append(line)

    stacks = createStacks(cratesRaw, numStacks)
    moves = parseMoves(movesRaw)

    topCratesCrateMover9000 = topCrates(moves, stacks[:], False)
    topCratesCrateMover9001 = topCrates(moves, stacks[:], True)

    print(f'(CrateMover 9000) After the rearrangement procedure completes, what crate ends up on top of each stack? {topCratesCrateMover9000}')
    print(f'(CrateMover 9001) After the rearrangement procedure completes, what crate ends up on top of each stack? {topCratesCrateMover9001}')
