filepath = '/Users/michaeltaylor/Documents/Advent of Code 2022/Day 1/input.txt'

with open(filepath) as input:
    acc, calories = 0, []
    
    for line in input:
        try:
            acc += int(line)
        except ValueError:
            calories.append(acc)
            acc = 0

    if acc > 0:
        calories.append(acc)

    mostCalories = max(calories)
    sumThreeMostCalories = sum(sorted(calories)[-3:])

    print(f'The most calories carried by an elf: {mostCalories}')
    print(f'The sum of calories carried by the 3 elves carrying the most calories: {sumThreeMostCalories}')

    
        
        
