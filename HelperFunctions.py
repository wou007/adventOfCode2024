import os

def ReadInput(day_number):
    if os.path.isfile(f'Input/Day{day_number}.txt'):
        filePath = f'Input/Day{day_number}.txt'
    
    file = open(filePath, 'r')
    data = file.read()
    file.close()

    return data

def Create2DList(width,height,initValue = 0):
    result = []
    for i in range(height):
        result.append([initValue for j in range(width)])
    return result
