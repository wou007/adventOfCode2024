import re

def Part1(f):
    res = 0

    for x in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',f.read()):
        res += int(x[0]) * int(x[1])    

    return res

def Part2(f):
    res = 0

    do = True

    for x in re.findall(r'(mul)\((\d{1,3}),(\d{1,3})\)|(don\'t)|(do)',f.read()):
        print(x)
        if x[3]:
            do = False
        if x[4]:
            do = True
        if x[0] and do:
            res += int(x[1]) * int(x[2])    

    return res

if __name__=="__main__":
    f = open('Input/Day3.txt','r')
    print('Part 1: ',Part1(f))
    f.seek(0)
    print('Part 2: ', Part2(f))
