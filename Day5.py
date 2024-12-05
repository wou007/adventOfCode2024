import re
import HelperFunctions
import itertools

day_number = 5

def Part1(f):
    res = 0

    rules = []
    pages = []

    for l in f.splitlines():
        if '|' in l:
            rules.append([int(x) for x in l.split('|')])
        elif ',' in l:
            pages.append([int(x) for x in l.split(',')])

    for page in pages:
        valid = True
        for r in rules:
            if r[0] in page and r[1] in page:
                if page.index(r[0]) > page.index(r[1]):
                    valid = False
                    break
        if valid:
            res += int(page[int((len(page))/2)])

    return res

def Part2(f):
    res = 0

    rules = []
    pages = []

    for l in f.splitlines():
        if '|' in l:
            rules.append([int(x) for x in l.split('|')])
        elif ',' in l:
            pages.append([int(x) for x in l.split(',')])

    for page in pages:
        onceInvalid = False
        valid = False
        while not valid:
            valid = True
            for r in rules:
                if r[0] in page and r[1] in page:
                    a = page.index(r[0])
                    b = page.index(r[1])
                    if a > b:
                        onceInvalid = True
                        valid = False
                        page.insert(b,page.pop(a))
        if onceInvalid:
            res += int(page[int((len(page))/2)])

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')