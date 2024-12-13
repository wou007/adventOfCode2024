import re
import HelperFunctions

day_number = 13

def FindCost(a,b,prize):
    A = abs((prize[0] * b[1] - prize[1] * b[0]) / (a[0]*b[1] - a[1]*b[0]))
    B = abs((prize[0] * a[1] - prize[1] * a[0]) / (a[0]*b[1] - a[1]*b[0]))

    if (A).is_integer() and (B).is_integer():
        return int(A * 3 + B)

    return 0

def FindCostOld(a,b,prize):
    aCount = 0
    bCount = 0
    
    bCount = int(prize[0] / b[0]) + 1
    while bCount > 0:
        x = aCount * a[0] + bCount * b[0]
        y = aCount * a[1] + bCount * b[1]
        if x == prize[0] and y == prize[1]:
            return aCount * 3 + bCount
        elif x > prize[0] or y > prize[1]:
            bCount-=1
        elif x < prize[0] or y < prize[1]:
            aCount+=1
    return 0

def Part1(f):
    res = 0

    butA = None
    butB = None
    prize = None
    for l in f.splitlines():
        a = re.match(r'Button A: X\+(\d+), Y\+(\d+)',l)
        b = re.match(r'Button B: X\+(\d+), Y\+(\d+)',l)
        p = re.match(r'Prize: X=(\d+), Y=(\d+)',l) 
        
        if a:
            butA = [int(a[1]),int(a[2])]
        if b:
            butB = [int(b[1]),int(b[2])]
        if p:
            prize = [int(p[1]),int(p[2])]
            res += FindCost(butA,butB,prize)

    return res

def Part2(f):
    res = 0

    butA = None
    butB = None
    prize = None
    for l in f.splitlines():
        a = re.match(r'Button A: X\+(\d+), Y\+(\d+)',l)
        b = re.match(r'Button B: X\+(\d+), Y\+(\d+)',l)
        p = re.match(r'Prize: X=(\d+), Y=(\d+)',l) 
        
        if a:
            butA = [int(a[1]),int(a[2])]
        if b:
            butB = [int(b[1]),int(b[2])]
        if p:
            prize = [int(p[1]) + 10000000000000,int(p[2]) + 10000000000000]
            res += FindCost(butA,butB,prize)

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')