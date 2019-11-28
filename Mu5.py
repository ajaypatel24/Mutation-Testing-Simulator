#simple standard deviation function

import math

def stdev (array):
    if (len(array) == 0):
        return 0

    mean = 0.0
    std = 0.0

    for x in array:
        mean += x
    
    mean /= len(array)

    for x in array:
        q = (x - mean)
        std += pow(q, 2)

    std = math.sqrt((std / len(array))) 
    std *= 10.0
    std /= 10.0
    return round(std, 2)



print(stdev([6,2,3,1]))