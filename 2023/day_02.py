#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:56:59 2023

@author: ari
"""

import re

data_file = open("day_02_data.txt", "r")

cubes = [12, 13, 14]

score = 0
cube_score = 0
data = {}

for game_id, value in enumerate(data_file.readlines()):
    temp = value.replace(" ", "")
    temp = re.sub("^[^:]*", "", temp)
    temp = temp.strip("\n")
    game = temp[1:].split(";")
    game_pass = True
    cube_temp_score = {"red" : 0, "green": 0, "blue": 0}
    #print("Game ID: " + str(game_id))
    for rounds in game:
        rolls = rounds.split(",")
        for roll in rolls:
            if roll[-1] == "d":
                if int(roll[:-3]) > cubes[0]:
                    #print("Red: " + roll[:-3])
                    game_pass = False
                if cube_temp_score["red"]  < int(roll[:-3]):
                    cube_temp_score["red"] = int(roll[:-3])
            if roll[-1] == "n":
                if int(roll[:-5]) > cubes[1]:
                    #print("Green: " + roll[:-5])
                    game_pass = False
                if cube_temp_score["green"]  < int(roll[:-5]):
                    cube_temp_score["green"]  = int(roll[:-5])
            if roll[-1] == "e":
                if int(roll[:-4]) > cubes[2]:
                    #print("Blue: " + roll[:-4])
                    game_pass = False
                if cube_temp_score["blue"] < int(roll[:-4]):
                    cube_temp_score["blue"] = int(roll[:-4])
                
    if game_pass:
        score = score + game_id + 1
    temp_score = cube_temp_score["red"] * cube_temp_score["green"]  * cube_temp_score["blue"] 
    print("Game ID: " + str(game_id + 1) + " Score: " + str(temp_score))
    cube_score = cube_score + temp_score
print(cube_score)