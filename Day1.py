import re

def Part1(f):
    res = 0

    left = []
    right = []

    for l in f.readlines():
        m = re.match('(\d+)   (\d+)',l)
        left.append(int(m[1]))
        right.append(int(m[2]))

    left.sort()
    right.sort()

    for a,b in zip(left,right):
        res += abs(a-b)

    return res

def Part2(f):
    res = 0

    left = []
    right = []

    for l in f.readlines():
        m = re.match('(\d+)   (\d+)',l)
        left.append(int(m[1]))
        right.append(int(m[2]))

    for i in left:
        res += right.count(i) * i

    return res

if __name__=="__main__":
    f = open('Input/Day1.txt','r')
    print('Part 1: ',Part1(f))
    f.seek(0)
    print('Part 2: ', Part2(f))
