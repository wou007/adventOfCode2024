import re
import HelperFunctions

day_number = 9

def Part1(f):
    res = 0

    for l in f.splitlines():
        l = [int(x) for x in l]
        s = []
        count = 0
        dot = False
        for x in l:
            for i in range(x):
                if dot:
                    s.append(None)
                else:
                    s.append(count)
            if not dot:
                count += 1
            dot = not dot

        while None in s:
            i = s.index(None)
            while None == s[-1]:
                s.pop()

            s[i] = s.pop()

            while None == s[-1]:
                s.pop()
        
        print(s)

        for a,b in zip(range(len(s)),s):
            res+= a*b

    return res

def Part2(f):
    res = 0

    

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')