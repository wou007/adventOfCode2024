import re

def Part1(f):
    res = 0

    for l in f.readlines():
        res+=1

    return res

def Part2(f):
    res = 0

    return res

if __name__=="__main__":
    f = open('Input/Day1.txt','r')
    print('Part 1: ',Part1(f))
    f.seek(0)
    print('Part 2: ', Part2(f))
