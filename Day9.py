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

        for a,b in zip(range(len(s)),s):
            res += a*b

    return res

def Part2(f):
    res = 0

    for l in f.splitlines():
        l = [int(x) for x in l]
        s = []
        count = 0
        dot = False
        for x in l:
            if dot:
                s.append([None,x,False])
            else:
                s.append([count,x,False])
            if not dot:
                count += 1
            dot = not dot

        for i in range(len(s)-1,-1,-1):
            if s[i][0] != None and s[i][2] == False:
                for a in range((len(s) - (len(s) -i)) + 1):
                    if s[a][0] == None and s[a][1] >= s[i][1]:
                        if s[a][1] == s[i][1]:
                            s[a][0] = s[i][0]
                            s[a][2] = True
                            s[i][0] = None
                        else:
                            copy = s[i].copy()
                            copy[2] = True
                            s[a][1] -= s[i][1]
                            s[i][0] = None
                            s.insert(a,copy)
                        break

        pos = 0

        for x in s:
            for i in range(x[1]):
                if x[0] != None:
                    res += pos*x[0]
                pos+=1

    return res

if __name__=="__main__":
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')