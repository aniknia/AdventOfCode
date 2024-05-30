#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:49:30 2023

@author: ari
"""

data = open("day_03_data.txt", "r")

dataLines = data.readlines()

col = len(dataLines)
row = len(dataLines[0]) - 1

print("Col: " + str(col) + " Row: " + str(row))

sum = 0

for y, line in enumerate(dataLines):
    for x, char in enumerate(line):
        if(char == "*"):
            if((x > 0 and x < row) and (y > 0 and y < col)):
                print("y\n")
            print("X: " + str(x) + " Y: " + str(y) + " Data: " + str(dataLines[x][y]))