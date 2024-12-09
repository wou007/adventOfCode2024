import re
import HelperFunctions

day_number = 8

def Part1(f):

    keys = {}

    y = 0

    width = 0

    for l in f.splitlines():
        width = len(l)
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
                    if a[0] < b[0]:
                        y1 = a[0] - deltaY
                        y2 = b[0] + deltaY
                    else:
                        y1 = a[0] + deltaY
                        y2 = b[0] - deltaY

                    if not [x1,y1] in news:
                        if x1 >= 0 and x1 < width and y1 >= 0 and y1 < y:
                            news.append([x1,y1])
                    if not [x2,y2] in news:
                        if x2 >= 0 and x2 < width and y2 >= 0 and y2 < y:
                            news.append([x2,y2])

    return len(news)

def Part2(f):
    keys = {}

    y = 0

    width = 0

    for l in f.splitlines():
        width = len(l)
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
            if len(ant) > 1:
                if not [a[1],a[0]] in news:
                    news.append([a[1],a[0]])
            for b in ant:
                if a != b:
                    x1 = a[1] 
                    y1 = a[0]
                    x2 = b[1]
                    y2 = b[0]
                    do = True
                    deltaX = abs(a[1]-b[1])
                    deltaY = abs(a[0]-b[0])
                    while do:
                        do = False
                        if a[1] < b[1]: #X
                            x1 -= deltaX
                            x2 += deltaX
                        else:
                            x1 += deltaX
                            x2 -= deltaX
                        if a[0] < b[0]:
                            y1 -= deltaY
                            y2 += deltaY
                        else:
                            y1 += deltaY
                            y2 -= deltaY

                        
                        if x1 >= 0 and x1 < width and y1 >= 0 and y1 < y:
                            if not [x1,y1] in news:
                                news.append([x1,y1])
                            do = True
                        if x2 >= 0 and x2 < width and y2 >= 0 and y2 < y:
                            if not [x2,y2] in news:
                                news.append([x2,y2])
                            do = True

    return len(news)

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')