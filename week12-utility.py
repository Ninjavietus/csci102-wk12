#John Robert
#CSCI 102 - Section E
#Week 12 Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as file:
        global lines
        lines = file.readlines()
        
