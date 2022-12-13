import json

pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 13/input.txt'

DIVIDER_PACKETS = [[[2]], [[6]]]

def makePairs(packets):
    i, pairs = 0, []
    while i < len(packets):
        pairs.append((packets[i], packets[i+1]))
        i += 2
    return pairs

def inspectPair(pair):
    packet1, packet2 = pair

    while packet1 and packet2:
        left, right = packet1[0], packet2[0]
        if type(left) == int and type(right) == int:
            if left < right:
                return True
            elif left > right:
                return False
        elif type(left) == list and type(right) == list:
            listComp = inspectPair((left, right))
            if listComp != None:
                return listComp
        else:
            if type(left) == int:
                left = [left]
            else:
                right = [right]
                
            comp = inspectPair((left, right))
            if comp != None:
                return comp

        packet1, packet2 = packet1[1:], packet2[1:]

    if (not packet1) and packet2:
        return True
    elif packet1 and not packet2:
        return False

def inspectPairs(packets):
    pairs = makePairs(packets)
    comparisons = [inspectPair(pair) for pair in pairs]

    sum = 0
    for i in range(len(comparisons)):
        if comparisons[i]:
            sum += i + 1
    return sum

def mergeSort(packets):
    length = len(packets)
    if len(packets) > 1:
        mid = length //2
        L, R = packets[:mid], packets[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if inspectPair((L[i], R[j])):
                packets[k] = L[i]
                i += 1
            else:
                packets[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            packets[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            packets[k] = R[j]
            j += 1
            k += 1

def getDecoderKey(packets):
    allPackets = packets + DIVIDER_PACKETS
    mergeSort(allPackets)

    return allPackets.index(DIVIDER_PACKETS[0]) * allPackets.index(DIVIDER_PACKETS[1])

    i = index1 = index2 = 0
    while i < len(allPackets):
        if allPackets[i] == DIVIDER_PACKETS[0]:
            index1 = i + 1
        elif allPackets[i] == DIVIDER_PACKETS[1]:
            index2 = i + 1
        i += 1

    return index1 * index2
    

with open(pathname) as input:
    packets = [json.loads(line.strip()) for line in input if line.strip()]
    
    print(f'What is the sum of the indices of those pairs? {inspectPairs(packets)}')
    print(f'What is the decoder key for the distress signal? {getDecoderKey(packets)}')
