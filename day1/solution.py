

def part1():

    input = open('input.txt', 'r')
    lines = input.readlines()


    total = 0

    for line in lines:
        nums = []
        for char in line.strip():
            if char.isnumeric():
                nums.append(char)
        total = total + int(nums[0] + nums[-1])
    return str(total) 


def part2():
    input = open('input.txt', 'r')
    lines = input.readlines()

    validDigits = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
                    "6": "6", "7":"7", "8":"8", "9": "9", "one": "1", "two": "2", "three": "3", 
                    "four": "4", "five": "5", "six": "6",
                   "seven": "7", "eight": "8", "nine": "9"}
    total = 0
    
    for line in lines:
        line = line.strip()
        firstIndex = len(line)
        lastIndex = -1
        firstVal = None
        lastVal = None
        for digit in list(validDigits.keys()):
            if digit in line:
                firstOccurence = line.find(digit)
                lastOccurence = line.rindex(digit)
                if firstOccurence >= 0 and firstOccurence < firstIndex:
                    firstIndex = firstOccurence
                    firstVal = validDigits[digit]
                if lastOccurence > lastIndex:
                    lastIndex = lastOccurence
                    lastVal = validDigits[digit]  
        total = total + int(firstVal + lastVal)
    return str(total)

print('Part 1: ' + part1())
print('Part 2: ' + part2())