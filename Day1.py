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

    for i in range(len(left)):
        res += abs(left[i]-right[i])

    return res

def Part2(f):
    res = 0

    left = []
    right = []

    for l in f.readlines():
        m = re.match('(\d+)   (\d+)',l)
        left.append(int(m[1]))
        right.append(int(m[2]))

    left.sort()
    right.sort()

    for i in left:
        res += right.count(i) * i

    return res

if __name__=="__main__":
    f = open('Input/Day1.txt','r')
    print('Part 1: ',Part1(f))
    f.seek(0)
    print('Part 2: ', Part2(f))
