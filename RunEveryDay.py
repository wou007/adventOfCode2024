import time

import HelperFunctions

import Day1
import Day2
import Day3
import Day4
import Day5

RUNS_FOR_TIMING = 5

if __name__ == "__main__":
    days = [Day1, Day2, Day3, Day4, Day5]
    
    totalStart = time.time()
    totalTime = 0
    for d in days:
        input = HelperFunctions.ReadInput(d.day_number)

        if input != None:
            startTime = time.time()
            d.Part1(input)
            for x in range(RUNS_FOR_TIMING):
                result1 = d.Part1(input)
            part1Time = time.time() - startTime
                            
            startTime = time.time()
            d.Part2(input)
            for x in range(RUNS_FOR_TIMING):
                result2 = d.Part2(input)
            part2Time = time.time() - startTime

            part1Time /= RUNS_FOR_TIMING
            part2Time /= RUNS_FOR_TIMING

            print(f'Day {d.day_number}') 
            print(f'    Duration part 1 - {round(part1Time*1000,1)}ms\tAnswer: {result1}')
            print(f'    Duration part 2 - {round(part2Time*1000,1)}ms\tAnswer: {result2}\n')

            totalTime += part1Time + part2Time
        else:
            print(f'Day {d.day_number} NO INPUT\n')

    print(f'Total Time: {round(time.time() - totalStart,3)} without IO: {round(totalTime,3)}s')