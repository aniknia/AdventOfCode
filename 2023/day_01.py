#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:17:00 2023

@author: ari
"""

import re

data = open("day_01_testdata.txt", "r")

total = 0

def word_check(string):
    num_word = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_string = string
    for i in range(0,9):
        new_string = re.sub(num_word[i], num_num[i], new_string)
    
    return new_string
    
    

for string in data.readlines():
    new_string = word_check(string)
    num_string = ''.join(filter(str.isdigit, new_string))
    
    print("String: " + string + "New String: " + new_string + "Number: " + num_string)
    
    
    if len(num_string) >= 2:
        total = total + (int(num_string[0]) * 10) + int(num_string[-1])
        print("Larger that 2: " + num_string[0] + " " + num_string[-1])
    else:
        total = total + (int(num_string) * 10) + int(num_string)
        print("Less that 2: " + num_string)
        
        
print(total)
