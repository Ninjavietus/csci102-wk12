#John Robert
#CSCI 102 - Section E
#Week 12 Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as file:
        global lines
        lines = file.readlines()

def UpdateString(string_1, string_2, integer):
    global new_list
    new_list = list(string_1)
    new_list[integer] = string_2
    new_string = ''.join(new_list)
    print('OUTPUT', new_string)
        
