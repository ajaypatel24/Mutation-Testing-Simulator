import os
import shutil 




#import Mutant1 #run file within another file


def findOperator(string):
    operators = "+-*/"
    
    for x in operators:
        if (x in string):
            return x
            


def generate_report():
    FaultList = open("FaultList.txt","w+")
    if not os.path.exists("Mutations"):
        os.mkdir("Mutations")
    
    stdev = open("stdev.py", "r")
    chars = ["+", "/", "-","=="]
    mutants = "+/-*"
    
    data = stdev.read().split('\n')
    lines = []
    mutations = []
    for x, l in enumerate(data):
        if (len(l.strip()) != 0):
            lines.append(l.strip())
        if (len(l.strip()) != 0 and any(z in l.strip() for z in mutants)):
            mutations.append(l.strip())
            FaultList.write(str(x))
            FaultList.write(":")
            FaultList.write(l.strip()+"\n")
            op = findOperator(l.strip())
            for y in mutants:
                if ( y != op):
                    FaultList.write(l.strip().replace(op,y) + "\n")
            

    for x in mutations:
        findOperator(x)
        
            
    print(mutations)


    mutants = len(mutations) * 3 + 1 #number of mutations for full coverage
    src = os.path.realpath("stdev.py")
    for y in mutations:
            for x in range(1,mutants):
                
                dst = "Mutant" + str(x) + ".py"
                shutil.copy(src,dst)
            
        





def delete():
    for x in range(1,22):
        os.remove("Mutant" + str(x) + ".py")
    #shutil.rmtree("Mutations")
    
    
    
                    


    


    
   


generate_report()
#delete() #remove directory with mutations inside
#fix()

