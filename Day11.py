import re
import HelperFunctions

day_number = 11

def Part1(f):
    res = 0

    numbers = {}

    for i in f.split():
        if int(i) not in numbers:
            numbers[int(i)] = 0
        numbers[int(i)] += 1

    for i in range(25):
        newStones = {}
        for n in numbers.keys():
            if n == 0:
                if 1 not in newStones:
                    newStones[1] = 0
                newStones[1] += numbers[n]
            elif len(str(n)) % 2 == 0:
                newLen = int(len(str(n)) / 2)
                num1 = int(str(n)[0:newLen])
                num2 = int(str(n)[newLen::])
                if num1 not in newStones:
                    newStones[num1] = 0
                if num2 not in newStones:
                    newStones[num2] = 0
                newStones[num1] += numbers[n]
                newStones[num2] += numbers[n]
            else:
                num = n * 2024
                if num not in newStones:
                    newStones[num] = 0
                newStones[num] += numbers[n]
        numbers = newStones.copy()

    for x in numbers:
        res+= numbers[x]

    return res

def Part2(f):
    res = 0

    numbers = {}

    for i in f.split():
        if int(i) not in numbers:
            numbers[int(i)] = 0
        numbers[int(i)] += 1

    for i in range(75):
        newStones = {}
        for n in numbers.keys():
            if n == 0:
                if 1 not in newStones:
                    newStones[1] = 0
                newStones[1] += numbers[n]
            elif len(str(n)) % 2 == 0:
                newLen = int(len(str(n)) / 2)
                num1 = int(str(n)[0:newLen])
                num2 = int(str(n)[newLen::])
                if num1 not in newStones:
                    newStones[num1] = 0
                if num2 not in newStones:
                    newStones[num2] = 0
                newStones[num1] += numbers[n]
                newStones[num2] += numbers[n]
            else:
                num = n * 2024
                if num not in newStones:
                    newStones[num] = 0
                newStones[num] += numbers[n]
        numbers = newStones.copy()

    for x in numbers:
        res+= numbers[x]

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')