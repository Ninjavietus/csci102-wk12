#https://github.com/Ninjavietus/csci102-wk12.git
#John Robert
#CSCI 102 - Section E
#Week 12 Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as file:
        global lines
        lines = file.readlines()
        return lines

def UpdateString(string_1, string_2, integer):
    global new_list
    new_list = list(string_1)
    new_list[integer] = string_2
    new_string = ''.join(new_list)
    print('OUTPUT', new_string)

def FindWordCount(in_list, string_in):
    for i in in_list:
        count = 0
        if i == string_in:
            count += 1
        return count

def ScoreFinder(player_names, player_scores, string_1):
    for i in player_names:
        if i == string_1:
            player = i
            score = int(player_scores[i])
            print('OUTPUT', player, 'got a score of', score)
        if string_1 is not in player_names:
            print('OUTPUT player not found')

def Union(list_1, list_2):
    for i in list_1:
        if i != list_2[i]:
            list_1.append(list_2[i])
        if i == list_2[i]:
            continue
    return list_1

def Intersection(list_1, list_2):
    list_new = []
    for i in list_1:
        if i == list_2[i]:
            list_new.append(list_2[i])
    return list_new

def NotIn(list_1, list_2):
    list_new_new = []
    for i in list_2:
        if i != list_1[i]:
            list_new_new.append(list_1[i])
    return list_new_new
    
        
