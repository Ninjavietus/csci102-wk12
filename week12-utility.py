#https://github.com/Ninjavietus/csci102-wk12.git
#John Robert
#CSCI 102 - Section E
#Week 12 Part B

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
    count = 0
    for i in in_list:
        if i == string_in:
            count += 1
    return count

def ScoreFinder(player_names, player_scores, string_1):
    for i in player_names:
        if i == string_1:
            for j in player_scores:
                score = j
                player = i
            print('OUTPUT', player, 'got a score of', score)
    if string_1 not in player_names:
        print('OUTPUT player not found')

def Union(list_1, list_2):
    new_list = list_1 + list_2
    for i in new_list:
        j = new_list.count(i)
        if j > 1:
            new_list.remove(i)
    return new_list

def Intersection(list_1, list_2):
    list_new = []
    for i in list_1:
        for j in list_2:
            if i == j:
                list_new.append(j)
    return list_new


def NotIn(list_2, list_1):
    for i in list_2:
        for j in list_1:
            if j == i:
                list_2.remove(i)
    return list_2
        
