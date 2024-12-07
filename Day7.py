import re
import HelperFunctions

day_number = 7

ADD = 0
MUL = 1
COMB = 2

def Part1Func(ans, ins, currentValue):
    res = 0
    for i in range(2):
        newCurrValue = currentValue
        if i == ADD:
            newCurrValue += ins[0]
        elif i == MUL:
            newCurrValue *= ins[0]
        
        if len(ins) == 1: #Last item
            if newCurrValue == ans:
                res += 1
        else:
            res += Part1Func(ans, ins[1::], newCurrValue)
    return res

def Part1(f):
    res = 0

    for l in f.splitlines():
        split = l.split(':')
        ans = int(split[0])
        ins = [int(x) for x in split[1].split()]
        
        if Part1Func(ans, ins[1::], ins[0]):
            res += ans

    return res

def Part2Func(ans, ins, currentValue):
    res = 0
    for i in range(3):
        newCurrValue = currentValue
        if i == ADD:
            newCurrValue += ins[0]
        elif i == MUL:
            newCurrValue *= ins[0]
        elif i == COMB:
            newCurrValue = int(str(newCurrValue) + str(ins[0]))
        
        if len(ins) == 1: #Last item
            if newCurrValue == ans:
                res += 1
        else:
            if(newCurrValue < ans):
                res += Part2Func(ans, ins[1::], newCurrValue)
    return res

def Part2(f):
    res = 0

    for l in f.splitlines():
        split = l.split(':')
        ans = int(split[0])
        ins = [int(x) for x in split[1].split()]
        
        if Part2Func(ans, ins[1::], ins[0]):
            res += ans
        
    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')