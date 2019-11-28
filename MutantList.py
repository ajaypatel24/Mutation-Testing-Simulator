import os
import shutil 







def findOperator(string):
    operators = "+-*/"
    
    for x in operators:
        if (x in string):
            return x
            


def generate_report():
    FaultList = open("FaultList.txt","w+")
    FaultUse = open("FaultUse.txt", "w+")
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
            #FaultList.write(str(x))
            #FaultList.write(":")
            FaultList.write(l.strip()+"\n")
            FaultUse.write(l+"\n")
            
            op = findOperator(l.strip())
            for y in mutants:
                if ( y != op):
                    FaultList.write(l.strip().replace(op,y) + "\n")
                    FaultUse.write(l.replace(op,y) +"\n")
            

    return mutations
        
            
def injectMutant(mutations):
    
    FaultUse = open("FaultUse.txt", "r")
    #mutants = len(mutations) * 3 + 1 #number of mutations for full coverage
    src = os.path.realpath("stdev.py")
    memory = "b"
    count = 0
    counter = 0
    for y in FaultUse:
            counter += 1
            stdev = open("stdev.py", "r")
            print("Back here:" + y)
            for z in stdev:
                
                print("y:" + y)
                print("z:" + z)
                

                if (y == z):
                    memory = y
                    break
                if (memory != "b"):
                    dst = "Mu" + str(counter) + ".py"
                    shutil.copy(src,dst)
                    Mutant = open(dst, "r")
                    dst1 = "Mutant" + str(counter) + ".py"
                    File = open(dst1, "w+")
                    for u in Mutant:
                        if (u == memory):
                            print("replacement made")
                            u = u.replace(u, y)
                        File.write(u)
                    count += 1
                    if (count == 3):
                        break
                    
                    
                        

                        
            
            
            '''
            print("mem:" + memory)
            dst = "Mu" + str(x) + ".py"
            shutil.copy(src,dst)
            Mutant = open(dst, "r")
            #print("Y:" + y)
            for z in Mutant:
                z = z.strip()
                if (len(z) == 0):
                    continue
                #print("Z:" + z)
                if (y.strip() == z):
                    print("Equality")
                    memory = z
                    break
                   
               ''' 

            
            

            
            
                
            
        





def delete():
    for x in range(1,22):
        os.remove("Mutant" + str(x) + ".py")
    #shutil.rmtree("Mutations")
    
    
    
                    


    


    
   


injectMutant(generate_report())
#delete() #remove directory with mutations inside
#fix()

