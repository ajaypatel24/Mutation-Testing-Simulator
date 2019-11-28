#simple standard deviation function

import math
import sys

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
    std -= 10.0
    
    print(round(std, 2))


def main(): 
    test = []
    for i in range(1, (len(sys.argv) -1)):
        test.append(float(sys.argv[i]))

    stdev(test)
    sys.exit


if __name__ == "__main__":
    main()

