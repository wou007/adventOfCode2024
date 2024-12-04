import re
import HelperFunctions

day_number = 3

def Part1(f):
    return sum([(int(x[0])*int(x[1])) for x in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',f)])  

def Part2(f):
    res = 0

    do = True

    for x in re.findall(r'(mul)\((\d{1,3}),(\d{1,3})\)|(don\'t\(\))|(do\(\))',f):
        if x[3]:
            do = False
        if x[4]:
            do = True
        if x[0] and do:
            res += int(x[1]) * int(x[2])    

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
