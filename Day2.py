import re

def Part1(f):
    res = 0

    for l in f.readlines():
        safe = True
        s = l.split()
        last = int(s[1])
        first = int(s[0])
        asdes = first - last
        if abs(first - last) > 3 or abs(first - last) < 1:
            continue
        for n in s[2::]:
            n = int(n)
            if abs(last-n) > 3 or abs(last-n) < 1:
                safe = False
            if asdes < 0 and last - n >= 0:
                safe = False
            if asdes > 0 and last - n <= 0:                
                safe = False
            last = n
        if safe:
            res += 1


    return res

def Part2(f):
    res = 0

    for l in f.readlines():
        safe = True
        s = l.split()
        s = [int(x) for x in s]
        last = int(s[1])
        first = int(s[0])
        if not (s == sorted(s) or s == sorted(s, reverse=True)):
            safe = False
        for n in s[2::]:
            n = int(n)
            if abs(last-n) > 3 or abs(last-n) < 1:
                safe = False
            last = n
        if safe:
            res += 1
        else:
            for i in range(len(s)):
                s2 = s.copy()
                s2.pop(i)
                safe = True
                last = int(s2[1])
                first = int(s2[0])
                if not (s2 == sorted(s2) or s2 == sorted(s2, reverse=True)):
                    safe = False
                if abs(first - last) > 3 or abs(first - last) < 1:
                    safe = False
                for n in s2[2::]:
                    n = int(n)
                    if abs(last-n) > 3 or abs(last-n) < 1:
                        safe = False
                    last = n
                if safe:    
                    res += 1
                    break

    return res

if __name__=="__main__":
    f = open('Input/Day2.txt','r')
    print('Part 1: ',Part1(f))
    f.seek(0)
    print('Part 2: ', Part2(f))
