# Incremental Build Model
# Michael Sprauer
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT', string)
    return

def LoadFile(filename):
    return_list = []
    with open(filename, 'r') as f:
        for line in f:
            return_list.append(line[:-1])
            
    return return_list

def UpdateString(str1,str2,x):
    str3 = str1[0:x] + str2 + str1[x+1:]
    print('OUTPUT',str3)


def FindWordCount(my_list,str1):

    return my_list.count(str1)

    
    
    
    
        
        
    
