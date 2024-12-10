import re
import HelperFunctions
import copy

day_number = 10

def IsInField(y, x, field):
    if y >= 0 and y < len(field) and x >= 0 and x < len(field[y]):
        return True
    return False

def FindTopsForLocation1(y, x, field):
    res = 0
    if IsInField(y+1, x, field):
        if field[y][x] + 1 == field[y+1][x]:
            if field[y+1][x] == 9:
                res += 1
                field[y+1][x] = 9001
            else:
                res += FindTopsForLocation1(y+1,x,field)

    if IsInField(y-1, x, field):
        if field[y][x] + 1 == field[y-1][x]:
            if field[y-1][x] == 9:
                res += 1
                field[y-1][x] = 9001
            else:
                res += FindTopsForLocation1(y-1,x,field)

    if IsInField(y, x+1, field):
        if field[y][x] + 1 == field[y][x+1]:
            if field[y][x+1] == 9:
                res += 1
                field[y][x+1] = 9001
            else:
                res += FindTopsForLocation1(y,x+1,field)

    if IsInField(y, x-1, field):
        if field[y][x] + 1 == field[y][x-1]:
            if field[y][x-1] == 9:
                res += 1
                field[y][x-1] = 9001
            else:
                res += FindTopsForLocation1(y,x-1,field)
    
    return res

def Part1(f):
    res = 0

    field = []

    for l in f.splitlines():
        field.append([int(x) for x in l])

    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 0:
                res += FindTopsForLocation1(y, x, copy.deepcopy(field))

    return res

def FindTopsForLocation2(y, x, field):
    res = 0
    if IsInField(y+1, x, field):
        if field[y][x] + 1 == field[y+1][x]:
            if field[y+1][x] == 9:
                res += 1
            else:
                res += FindTopsForLocation2(y+1,x,field)

    if IsInField(y-1, x, field):
        if field[y][x] + 1 == field[y-1][x]:
            if field[y-1][x] == 9:
                res += 1
            else:
                res += FindTopsForLocation2(y-1,x,field)

    if IsInField(y, x+1, field):
        if field[y][x] + 1 == field[y][x+1]:
            if field[y][x+1] == 9:
                res += 1
            else:
                res += FindTopsForLocation2(y,x+1,field)

    if IsInField(y, x-1, field):
        if field[y][x] + 1 == field[y][x-1]:
            if field[y][x-1] == 9:
                res += 1
            else:
                res += FindTopsForLocation2(y,x-1,field)
    
    return res

def Part2(f):
    res = 0

    field = []

    for l in f.splitlines():
        field.append([int(x) for x in l])

    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 0:
                res += FindTopsForLocation2(y, x, copy.deepcopy(field))

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')