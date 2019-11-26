f = open("FaultList.txt", "w+")
u = open("Mutants.txt","w+")


#import Mutant1 #run file within another file


stdev = open("stdev.py", "r")
chars = ["+", "/", "-","=="]
mutants = ["+", "/", "-", "*"]
f.write("FAULT LIST\n")
with stdev as stdev:
    line = stdev.readline()
    cnt = 1
    while line: 
        for x in line: 
            for y in chars:
                if (x == y):
                    f.write(str(cnt))
                    f.write(':')
                    f.write(y)
                    f.write("\n")
                    for z in mutants:
                        if (y != z):
                            u.write(z)
                    u.write("\n")

        line = stdev.readline()
        cnt += 1
        