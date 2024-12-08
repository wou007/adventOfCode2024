import re
import HelperFunctions

day_number = 8

def Part1(f):
    res = 0

    keys = {}

    y = 0

    for l in f.splitlines():
        for x in range(len(l)):
            if l[x] != '.':
                if not l[x] in keys:
                    keys[l[x]] = []
                keys[l[x]].append([y,x])
        y+=1

    news = []

    for k in keys:
        ant = keys[k]
        for a in ant:
            for b in ant:
                if a != b:
                    x1 = 0
                    y1 = 0
                    x2 = 0
                    y2 = 0
                    deltaX = abs(a[1]-b[1])
                    deltaY = abs(a[0]-b[0])
                    if a[1] < b[1]: #X
                        x1 = a[1] - deltaX
                        x2 = b[1] + deltaX
                    else:
                        x1 = a[1] + deltaX
                        x2 = b[1] - deltaX
                    if a[0] < b[1]:
                        y1 = a[0] - deltaY
                        y2 = b[0] + deltaY
                    else:
                        y1 = a[0] + deltaY
                        y2 = b[0] - deltaY
 
                    news.append([x1,y1])
                    news.append([x2,y2])

    return res

def Part2(f):
    res = 0

    

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')