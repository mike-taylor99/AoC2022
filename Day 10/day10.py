pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 10/input.txt'

SIGNALSTRENGTHCYCLES = [20, 60, 100, 140, 180, 220]

def performOp(instruction, X):
    length = len(instruction)

    if length == 1 and instruction[0] == 'noop':
        return [X]
    elif length == 2 and instruction[0] == 'addx':
        return [X, X + instruction[1]]

def performOps(instructions):
    X = 1
    cycles = []

    for instruction in instructions:
        cycles += performOp(instruction, X)
        X = cycles[-1]

    return cycles

def drawCRT(cycles):
    CRT = ''
    shiftCyclesRight = [1] + cycles
    
    for i in range(240):
        if i%40 == 0 and i != 0:
            CRT += '\n'

        cycle = shiftCyclesRight[i]
        if i%40 in range(cycle-1, cycle+2):
            CRT += '#'
        else:
            CRT += '.'

    return CRT

with open(pathname) as input:
    program = [line.strip().split(' ') for line in input]
    program = [instruction if len(instruction) == 1 else [instruction[0], int(instruction[1])] for instruction in program]

    cycles = performOps(program)

    sum = 0
    for cycle in SIGNALSTRENGTHCYCLES:
        sum += cycle * cycles[cycle-1]
    
    print(f'What is the sum of these six signal strengths? {sum}')

    print(f'What eight capital letters appear on your CRT? \n{drawCRT(cycles)}')
