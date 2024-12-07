import re
import HelperFunctions
import copy

day_number = 6

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def Part1(f):
    thing = []
    x = 0
    y = 0
    direction = UP

    for l in f.splitlines():
        if '^' in l:
            y = len(thing)
            x = l.index('^')

        thing.append(list(l))

    while x >= 0 and y >= 0 and x < len(thing[0]) and y < len(thing):
        nextX = x
        nextY = y
        if direction == UP:
            nextY -= 1
        if direction == DOWN:
            nextY += 1
        if direction == LEFT:
            nextX -= 1
        if direction == RIGHT:
            nextX += 1
        if nextX >= 0 and nextY >= 0 and nextX < len(thing[0]) and nextY < len(thing):
            if thing[nextY][nextX] == '#':
                direction = (direction + 1) % 4
            else:
                thing[y][x] = 'X'
                y = nextY
                x = nextX
        else:
            thing[y][x] = 'X'
            break
        

    return sum([l.count('X') for l in thing])

def IsThingLooping(thing, x, y):
    direction = UP
    repeatedVisitCounter = 0
    while x >= 0 and y >= 0 and x < len(thing[0]) and y < len(thing):
        nextX = x
        nextY = y
        if direction == UP:
            nextY -= 1
        if direction == DOWN:
            nextY += 1
        if direction == LEFT:
            nextX -= 1
        if direction == RIGHT:
            nextX += 1
        if nextX >= 0 and nextY >= 0 and nextX < len(thing[0]) and nextY < len(thing):
            if thing[y][x] == 'X':
                repeatedVisitCounter += 1
                if repeatedVisitCounter > 10000:
                    return True
            else:
                repeatedVisitCounter = 0
            if thing[nextY][nextX] == '#':
                direction = (direction + 1) % 4
            else:
                thing[y][x] = 'X'
                y = nextY
                x = nextX
        else:
            thing[y][x] = 'X'
            return False
    
    return False

def Part2(f):
    res = 0

    thing = []
    x = 0
    y = 0
    direction = UP

    for l in f.splitlines():
        if '^' in l:
            y = len(thing)
            x = l.index('^')

        thing.append(list(l))

    origThing = copy.deepcopy(thing)
    origX = x
    origY = y

    while x >= 0 and y >= 0 and x < len(thing[0]) and y < len(thing):
        nextX = x
        nextY = y
        if direction == UP:
            nextY -= 1
        if direction == DOWN:
            nextY += 1
        if direction == LEFT:
            nextX -= 1
        if direction == RIGHT:
            nextX += 1
        if nextX >= 0 and nextY >= 0 and nextX < len(thing[0]) and nextY < len(thing):
            if thing[nextY][nextX] == '#':
                direction = (direction + 1) % 4
            else:
                thing[y][x] = 'X'
                y = nextY
                x = nextX
        else:
            thing[y][x] = 'X'
            break

    for ty in range(len(thing)):
        for tx in range(len(thing[0])):
            if thing[ty][tx] == 'X':
                copyThing = copy.deepcopy(origThing)
                copyThing[ty][tx] = '#'
                if IsThingLooping(copyThing,origX,origY):
                    res += 1

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')