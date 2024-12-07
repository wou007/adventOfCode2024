import re
import HelperFunctions

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
            if thing[nextY][nextX] != '.':
                if thing[nextY][nextX] == '#':
                    direction = (direction + 1) % 4
                else:
                    if thing[nextY][nextX] == '^' and direction == LEFT:
                        res += 1
                        [print(''.join(l)) for l in thing]
                        print('')
                    if thing[nextY][nextX] == '>' and direction == UP:
                        res += 1
                        [print(''.join(l)) for l in thing]
                        print('')
                    if thing[nextY][nextX] == '<' and direction == DOWN:
                        res += 1
                        [print(''.join(l)) for l in thing]
                        print('')
                    if thing[nextY][nextX] == 'V' and direction == RIGHT:
                        res += 1
                        [print(''.join(l)) for l in thing]
                        print('')
            if thing[nextY][nextX] != '#':
                if direction == UP:
                    thing[y][x] = '^'
                if direction == DOWN:
                    thing[y][x] = 'V'
                if direction == LEFT:
                    thing[y][x] = '<'
                if direction == RIGHT:
                    thing[y][x] = '>'
                y = nextY
                x = nextX
        else:
            break

    # [print(''.join(l)) for l in thing]

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')