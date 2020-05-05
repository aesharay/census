# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:11:14 2020

@author: aesha
"""

###########################################################
    #Computer Project #7
    #   open_file function
    #   calc_multipliers function
    #   calc_priorities function
    #   read_file_make_priorities function
    #   add_to_state function
    #   display function
    #   printing all data through main function
###########################################################


import math
import csv

def open_file():
    '''Asking for a file name and opening file, otherwise print error'''
    fp = input("Enter filename: ") #prompt for file name
    while True:
        try:
            fp = open(fp, "r")
            return fp    
        except FileNotFoundError: #display error if file doesn't exist
            print("File not found! Please try again!")
            
def calc_multipliers():
    '''Calculate and return a list of multipliers'''
    n = 2
    calc_mult = []
    while n != 61: #loop through numbers between 2-60
        result = 1/(math.sqrt(n*(n-1)))
        calc_mult.append(result) #adding number to list
        n += 1 
    return calc_mult

    
def calc_priorities(s,p,m):
    '''Calculate and return priority list for each state'''
    s = str(s)
    p = int(p)
    prior = []
    for i in range(len(m)):
        prior.append((int(m[i]*p), s)) #adding each priority to one large list
    return prior

def read_file_make_priorities(fp,multipliers): 
    ''' Reads file, returns list of priorities and number of state reps '''
    fp.readline() #skip header
    state_reps = []
    priorities = []
    for line in fp: 
        line = line.split(',') #removing quotes and comma
        s = str(line[1].strip('" '))
        p = int(line[2].strip(' '))
        if s == "District of Columbia" or s == "Puerto Rico": #skip over DOC and PR
            continue
        prio = [s, 1]
        calc_prio = calc_priorities(s,p,multipliers) #Calling calc_priorities function
        priorities += calc_prio #adding priority list of each state to one large list
        state_reps.append(prio)
    state_reps.sort() #sorting and ordering both lists
    priorities.sort(reverse = True)
    priorities = priorities[:385]
    return state_reps, priorities

def add_to_state(state,states):
    '''Adding one to each representative count'''
    for i in range(len(states)):
        if states[i][0]==state:
            states[i][1] += 1 #adding one to each rep count

def display(states):
    '''Formating final list of states and its' reps'''
    print('\n{:<15s}{}'.format("State","Representatives")) #Formatting title
    for i in range(len(states)):
        print("{:<15s}{:>4d}".format(states[i][0],states[i][1])) #formatting the columns

def main():
    '''Executes all functions'''
    fp = open_file()
    m = calc_multipliers()
    states, prior = read_file_make_priorities(fp,m)
    for priority, state in prior:
        add_to_state(state,states)
    display(states)
    
if __name__ == "__main__":
    main()
    
    
    
    
    states = []
    for i in master_dict.keys():
        if country.lower() == i.lower():
            for val in master_dict[i]:
                val = list(val.keys())[0]
                states.append(val)
                set(states)
    return states


  fp = input("Data file: ") #prompt for file name
    if fp == '':
        fp = open('ncov.csv', "r")
    else:
        try:
            fp = open(fp, "r")
            return fp    
        except FileNotFoundError: #display error if file doesn't exist
            print("Error. Try again.")
            return open_file()