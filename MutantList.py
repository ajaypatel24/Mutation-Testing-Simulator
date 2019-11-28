import os
import shutil 
import subprocess

injectedFiles = []

def findOperator(string):
    operators = "+-*/"
    
    for x in operators:
        if (x in string):
            return x
            

#The following method will generate a list of all mutations sites and possible mutations on the operator 
def generateReport(): 
    FaultList = open("FaultList.txt","w+") #report (strip() used)
    FaultUse = open("FaultUse.txt", "w+") #will be used for injection (strip() not used)

    if not os.path.exists("Mutations"): #makes dir to hold mutation files
        os.mkdir("Mutations")
  
    
    stdev = open("stdev.py", "r") #open SUT
    mutants = "+/-*"
    
    data = stdev.read().split('\n')
    lines = []

    for x, l in enumerate(data):
        if (len(l.strip()) != 0):
            lines.append(l.strip())

        if (len(l.strip()) != 0 and any(z in l.strip() for z in mutants)): #if any of the lines contain an operator
            
            FaultList.write(">MUTATION SITE LINE " + str(x) + ": ") #adds mutation sites and list of possible mutations to FaultList.txt
            FaultList.write(l.strip() + "\n")
            
            
            FaultUse.write(l+"\n") #FaultUse.txt gets unstripped 
            
            op = findOperator(l.strip()) #get operator contained in line
            for y in mutants:
                if (y != op): #generate all possible mutations
                    FaultList.write(l.strip().replace(op,y) + "\n") #FaultList gets stripped version
                    FaultUse.write(l.replace(op,y) +"\n") #FaultUse gets unstripped 
            


#the following method injects the mutations created in generateReport into the SUT, each injection creates a new .py file 
#to run against the SUT to compare outputs
def injectMutant():
    
    FaultUse = open("FaultUse.txt", "r")
    src = os.path.realpath("stdev.py") #open SUT later on
    memory = "b" #default value for memory 
    count = 0 #each operator has 3 mutations 
    counter = 0 #universal counter for mutant ID and line number 
    for mu in FaultUse: #iterate through all mutations
            counter += 1
            stdev = open("stdev.py", "r")
            for z in stdev:
                if (mu == z):
                    memory = mu #keep the original line in memory
                    break
                if (memory != "b"):
                    SUT = open(src, "r")
                    dst1 = "Mutations/Mutant" + str(counter) + ".py" 
                    if(dst1 not in injectedFiles):
                        injectedFiles.append(dst1)
                    File = open(dst1, "w+") #create file with name dst1
                    for u in SUT: #copy SUT into mutated file
                        if (u == memory): #value in memory has 3 mutations associated, once this line is hit
                            u = u.replace(u, mu) #it is replaced with one of the 3 mutations
                        File.write(u)
                    count += 1
                    File.close()
                    SUT.close()
                    if (counter % 4 == 1): #some files get generated with a missplaced mutant because the mutant is equal to the SUT
                        os.remove(dst1) #remove these files
                    if (count == 3): #once 3 mutations have been inserted, change memory value by breaking loop
                        break
    
    #close all files to avoid run time errors
    File.close()
    SUT.close()
    FaultUse.close()
    stdev.close()
    os.remove("FaultUse.txt") #remove FaultUse.txt, it is no longer needed
                    
                  

    
    

def KillMutant(): 
    

    with open('FaultList.txt', 'r') as file:
        lines = file.readlines()

    validDeviation = subprocess.check_output("python stdev.py 5.5 6.7 8.9 4.3 5 6 1 4 3 1 23 9 2 4 5 1 0 4 2 7 9 2 3 5", shell=True)
    position = 0
    output = ""

    for injected in injectedFiles:

        #if(position == 32):
        #    print(injected)
        #    break

        if(">MUTATION SITE " in lines[position]):

            position += 1

        try:
            output = subprocess.check_output("python " + injected + " 5.5 6.7 8.9 4.3 5 6 1 4 3 1 23 9 2 4 5 1 0 4 2 7 9 2 3 5", shell=True)
        except (subprocess.CalledProcessError, ValueError, ZeroDivisionError) as e:
            output = "ERROR"

        if(output != validDeviation):
            lines[position] = lines[position].strip('\n') + " MUTANT KILLED\n"   
        else: 
            lines[position] += lines[position].strip('\n') + " MUTANT ALIVE\n"  

        position += 1
        
    
    with open('FaultList.txt', 'w') as file:
        file.writelines(lines)

    
                    


generateReport() #start by generating FaultUse.txt
injectMutant() #inject mutants using FaultUse.txt
KillMutant()

