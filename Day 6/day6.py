pathname = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 6/input.txt'

def indexAfterMarker(string, windowSize):
    length = len(string)
    for i in range(0, length - windowSize):
        window = inputString[i: i+windowSize]
        charSet = set([char for char in window])
        if len(charSet) == windowSize:
            return i + windowSize

with open(pathname) as input:
    inputString = input.readline()

    startOfPacket = indexAfterMarker(inputString, 4)
    startOfMessage = indexAfterMarker(inputString, 14)

    print(f'How many characters need to be processed before the first start-of-packet marker is detected? {startOfPacket}')
    print(f'How many characters need to be processed before the first start-of-message marker is detected? {startOfMessage}')
