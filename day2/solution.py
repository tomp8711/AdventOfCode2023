import re

def part1():

    input = open('input.txt', 'r')
    lines = input.readlines()
    total = 0
    for line in lines:
        line = re.split(r"Game (\d+): (.*)", line.strip())
        id = line[1]
        gameSets = line[2].split(';')
        possible = True
        for gameSet in gameSets:
            blue = re.search(r"(\d+) blue", gameSet)
            red = re.search(r"(\d+) red", gameSet)
            green = re.search(r"(\d+) green", gameSet)
            blueNum = int(blue.group(1)) if blue else 0
            redNum = int(red.group(1)) if red else 0
            greenNum = int(green.group(1)) if green else 0
            if blueNum > 14 or redNum > 12 or greenNum > 13:
                possible = False
        if possible:
            total += int(id)
    
    return total

def part2():

    input = open('input.txt', 'r')
    lines = input.readlines()
    total = 0
    for line in lines:
        blueMax = 0
        redMax = 0 
        greenMax = 0
        line = re.split(r"Game (\d+): (.*)", line.strip())
        gameSets = line[2].split(';')
        for gameSet in gameSets:
            blue = re.search(r"(\d+) blue", gameSet)
            red = re.search(r"(\d+) red", gameSet)
            green = re.search(r"(\d+) green", gameSet)
            blueNum = int(blue.group(1)) if blue else 0
            redNum = int(red.group(1)) if red else 0
            greenNum = int(green.group(1)) if green else 0
            blueMax = max(blueMax, blueNum)
            redMax = max(redMax, redNum)
            greenMax = max(greenMax, greenNum)
        total += blueMax * greenMax * redMax
    
    return total


print(part1())
print(part2())