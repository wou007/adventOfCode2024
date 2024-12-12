import re
import HelperFunctions

day_number = 12

def FindPotsInField(field, x, y):
    res = []
    res.append([x,y])
    char = field[y][x]
    field[y][x] = char.lower()
    tempY = y - 1
    tempX = x
    for tempX, tempY in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if tempY >= 0 and tempY < len(field) and tempX >= 0 and tempX < len(field[0]):
            if field[tempY][tempX] == char:
                res += FindPotsInField(field, tempX, tempY)

    return res


def FindRegions(field):
    res = []

    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x].isupper():
                res.append(FindPotsInField(field,x,y))

    return res

def CalculateBorderOfRegion(region):
    res = 0
    for x,y in region:
        for tempX, tempY in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if [tempX,tempY] not in region:
                res+=1
    return res


def Part1(f):
    res = 0

    field = []

    for l in f.splitlines():
        field.append(list(l))
    
    regions = FindRegions(field)

    for reg in regions:
        res += CalculateBorderOfRegion(reg) * len(reg)

    return res

def CalculateSidesOfRegion(region):
    res = 0
    for x,y in region:
        offsetPoints = [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
        for i in range(len(offsetPoints) - 1):
            if offsetPoints[i] not in region and offsetPoints[i-1] not in region:
                res+=1
        innerCornerChecks = [[[x+1,y+1],[x,y+1],[x+1,y]],
                             [[x-1,y+1],[x,y+1],[x-1,y]],
                             [[x-1,y-1],[x,y-1],[x-1,y]],
                             [[x+1,y-1],[x,y-1],[x+1,y]]]
        for i in innerCornerChecks:
            if i[0] not in region and i[1] in region and i[2] in region:
                res += 1
    return res

def Part2(f):
    res = 0

    field = []

    for l in f.splitlines():
        field.append(list(l))
    
    regions = FindRegions(field)

    for reg in regions:
        res += CalculateSidesOfRegion(reg) * len(reg)

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')