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
        
        
    
