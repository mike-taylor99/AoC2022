import copy
import math

pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 11/input.txt'

def buildMonkeyObjects(monkeyInput):
    monkeys = {}

    i = 0
    while i < len(monkeyInput):
        monkeyId = monkeyInput[i][-1].replace(':', '')
        i += 1

        items = [int(item.replace(',', '')) for item in monkeyInput[i][2:]]
        i += 1

        operation = monkeyInput[i][3:]
        i+= 1

        testDivisibleValue = int(monkeyInput[i][-1])
        i += 1

        trueCondition = monkeyInput[i][-1]
        i += 1

        falseCondition = monkeyInput[i][-1]

        monkeys[monkeyId] = {
                'id': monkeyId,
                'items': items,
                'operation': operation,
                'testDivisibleValue': testDivisibleValue,
                'trueCondition': trueCondition,
                'falseCondition': falseCondition,
                'numInspected': 0
            }
        i += 2

    return monkeys

def performOperation(old, operationList):
    if operationList[0] == 'old':
        val1 = old
    else:
        val1 = int(operationList[0])

    if operationList[-1] == 'old':
        val2 = old
    else:
        val2 = int(operationList[-1])

    if operationList[1] == '*':
        return val1 * val2
    elif operationList[1] == '+':
        return val1+ val2

def performRound(monkeys):
    for monkey in [str(i) for i in range(len(monkeys))]:
        items = monkeys[monkey]['items']
        for item in items:
            monkeys[monkey]['numInspected'] += 1
            new = performOperation(item, monkeys[monkey]['operation'])
            worryLevel = math.floor(new / 3)
            test = (worryLevel % monkeys[monkey]['testDivisibleValue']) == 0
            if test:
                monkeys[monkeys[monkey]['trueCondition']]['items'] += [worryLevel]
            else:
                monkeys[monkeys[monkey]['falseCondition']]['items'] += [worryLevel]
        monkeys[monkey]['items'] = []

def performRoundPart2(monkeys):
    reductor = 1
    for val in [monkeys[monkey]['testDivisibleValue'] for monkey in monkeys]:
        reductor *= val
    
    for monkey in [str(i) for i in range(len(monkeys))]:
        items = monkeys[monkey]['items']
        for item in items:
            monkeys[monkey]['numInspected'] += 1
            new = performOperation(item, monkeys[monkey]['operation'])
            worryLevel = new % reductor
            test = (worryLevel % monkeys[monkey]['testDivisibleValue']) == 0
            if test:
                monkeys[monkeys[monkey]['trueCondition']]['items'] += [worryLevel]
            else:
                monkeys[monkeys[monkey]['falseCondition']]['items'] += [worryLevel]
        monkeys[monkey]['items'] = []

def performRounds(monkeyInput, numRounds, performRoundFunc):
    monkeys = buildMonkeyObjects(monkeyInput)

    for i in range(numRounds):
        performRoundFunc(monkeys)

    numInspections = [monkeys[monkey]['numInspected'] for monkey in monkeys]
    numInspections.sort()

    return numInspections[-2] * numInspections[-1]
            
with open(pathname) as input:
    monkeyInput = [line.strip().split(' ') for line in input]
    
    part1 = performRounds(monkeyInput, 20, performRound)
    part2 = performRounds(monkeyInput, 10000, performRoundPart2)

    print(f'What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans? {part1}')
    print(f'What is the level of monkey business after 10000 rounds? {part2}')
