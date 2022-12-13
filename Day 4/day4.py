pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 4/input.txt'

with open(pathname) as input:
    totalSubsets, totalOverlaps = 0, 0
    
    for line in input:
        if '\n' in line:
            cleanedLine = line.replace('\n', '')
        else:
            cleanedLine = line
        
        pairs = cleanedLine.split(',')
        pairs = [sections.split('-') for sections in pairs]
        pairs = [[int(section) for section in sections] for sections in pairs]
        pairs = [set([x for x in range(sections[0], sections[1] + 1)]) for sections in pairs]

        isSubset = pairs[0].issubset(pairs[1]) or pairs[1].issubset(pairs[0])
        existsIntersection = len(pairs[0].intersection(pairs[1])) > 0

        totalSubsets += int(isSubset)
        totalOverlaps += int(existsIntersection)

    print(f'In how many assignment pairs does one range fully contain the other? {totalSubsets}')
    print(f'In how many assignment pairs do the ranges overlap? {totalOverlaps}')
