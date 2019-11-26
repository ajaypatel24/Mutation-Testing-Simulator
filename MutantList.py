f = open("FaultList.txt", "w+")
u = open("Mutants.txt","w+")

m = open("Mutants.txt", "r")


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
        

def fix():
    l = open("Mutant1.py", "w+")
    n = open("stdevcopy.py", "r")

    line1 = n.readline()
    while line1:
        for x in line1:
            for y in chars:
                if (x == y):
                    line1 = line1.replace(x, "/")
                    break
        l.write(line1)
        l.write("\n")
        line1 = n.readline()

    n.close
    l.close


fix()
f.close()
u.close()

m.close()
