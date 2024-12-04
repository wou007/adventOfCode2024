import re

def Part1(f):
    res = 0

    field = []

    for l in f.readlines():
        field.append(l)

    #horizontal
    for l in field:
        res += l.count('XMAS')
        res += l[::-1].count('XMAS')

    #vertical
    vertField = list(zip(*field))
    vertField = [str().join(x) for x in vertField]

    for l in vertField:
        res += l.count('XMAS')
        res += l[::-1].count('XMAS') 

    #diagonal start top left
    for i in range(-len(field),len(field[0])):
        y = 0
        x = i
        l = ''
        for j in range(len(field)):
            if x >= 0 and y >= 0:
                try:
                    l += field[y][x]
                except:
                    pass
            y+=1
            x+=1
        res += l.count('XMAS')
        res += l[::-1].count('XMAS') 

    for i in range(len(field[0]) + len(field), 0, -1):
        y = 0
        x = i
        l = ''
        for j in range(len(field)):
            if x >= 0 and y >= 0:
                try:
                    l += field[y][x]
                except:
                    pass
            y+=1
            x-=1
        print(l)
        res += l.count('XMAS')
        res += l[::-1].count('XMAS') 

    return res

def Part2(f):
    res = 0

    field = []

    for l in f.readlines():
        field.append(l)

    for y in range(1,len(field)-1):
        for x in range(1,len(field)):
            if field[y][x] == 'A':
                if field[y-1][x-1] == 'M' and field[y+1][x+1] == 'S':
                    if field[y-1][x+1] == 'M' and field[y+1][x-1] == 'S':
                        res += 1
                    if field[y-1][x+1] == 'S' and field[y+1][x-1] == 'M':
                        res += 1
                if field[y-1][x-1] == 'S' and field[y+1][x+1] == 'M':
                    if field[y-1][x+1] == 'M' and field[y+1][x-1] == 'S':
                        res += 1
                    if field[y-1][x+1] == 'S' and field[y+1][x-1] == 'M':
                        res += 1
                    
    return res

if __name__=="__main__":
    f = open('Input/Day4.txt','r')
    print('Part 1: ',Part1(f))
    f.seek(0)
    print('Part 2: ', Part2(f))
