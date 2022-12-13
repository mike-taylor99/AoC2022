pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 7/input.txt'

directory = {}

def updateSizes(curr, size):
    if '_size' in curr:
        curr['_size'] += size
    else:
        curr['_size'] = size

    if '_parent' in curr:
        updateSizes(curr['_parent'], size)

def sumTotalSizes(curr, max):
    sum = 0
    omitKeys = ['_isDir', '_parent', '_size']

    if curr.get('_isDir'):
        if curr['_size'] < max:
            sum += curr['_size']

    for key in curr:
        if key in omitKeys:
            continue
        sum += sumTotalSizes(curr[key], max)

    return sum

def findSmallestDirectoryToDelete(curr, outermostSize):
    target = 30000000 - (70000000 - outermostSize)
    sizes = [float('inf')]
    omitKeys = ['_isDir', '_parent', '_size']

    if curr.get('_isDir'):
        if curr['_size'] >= target:
            sizes += [curr['_size']]

    for key in curr:
        if key in omitKeys:
            continue
        sizes += [findSmallestDirectoryToDelete(curr[key], outermostSize)]

    return min(sizes)
    
    
with open(pathname) as input:
    lines = [line for line in input]
    i = 0

    parent, current = directory, directory
    while i < len(lines):
        command = lines[i].strip().replace('$ ', '')
        split = command.split(' ')

        if split[0].startswith('cd'):
            if split[1] == '/':
                parent, current = directory, directory
            elif split[1] == '..':
                if not (parent is directory):
                    parent = parent['_parent']
                if not (current is directory):
                    current = current['_parent']
            else:
                if not (split[1] in current):
                    current[split[1]] = {'_parent': current, '_isDir': True}
                parent, current = current, current[split[1]]
        elif split[0] == 'ls':
            i += 1
            while i < len(lines) and not lines[i].startswith('$'):
                split = lines[i].strip().split(' ')

                if split[0] == 'dir':
                    current[split[1]] = {'_parent': current, '_isDir': True}
                else:
                    current[split[1]] = {'_parent': current, '_size': int(split[0])}
                    updateSizes(current, int(split[0]))

                i += 1
            
            i -= 1

        i += 1

    totalSizes = sumTotalSizes(directory, 100000)
    smallestDirectoryToDelete = findSmallestDirectoryToDelete(directory, directory['_size'])

    print(f'What is the sum of the total sizes of those directories? {totalSizes}')
    print(f'What is the total size of that directory? {smallestDirectoryToDelete}')
