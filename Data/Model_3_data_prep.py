#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:04:35 2020

@author: lawrence
"""
import pandas as pd

salary_Data = pd.read_excel("Player_Salaries_1990_2017.xlsx")
season_Data = pd.read_csv("Seasons_Stats.csv")

#Filtering data between 1990-2017
season_Data = season_Data.loc[season_Data['Year']>=1990,:]
season_Data['Salary'] = 0

#Iterating over the season data and salary data to merge the two dfs into one df
# for i in range(0,15118):
#     for j in range(0, 11837):
player_index = []
year_index = []
for i in season_Data.index:
    for j in salary_Data.index:
        if(season_Data['Player'][i] == salary_Data['Player Name'][j]):
            if(season_Data['Year'][i] == salary_Data['Season Start'][j]):
                season_Data.loc[i,'Salary'] = salary_Data['Salary in $'][j]
            else:
                year_index.append(i)
        else:
            player_index.append(i)
            
year_index = set(year_index)

for i in year_index:
    for j in salary_Data.index:
        if(season_Data['Player'][i] == salary_Data['Player Name'][j]):
            if(season_Data['Year'][i] == salary_Data['Season End'][j]):
                season_Data.loc[i,'Salary'] = salary_Data['Salary in $'][j]
            else:
                print("Year=======>",i)
        else:
            print("Player Index=============>",i)
        
        
season_Data.to_csv('1990_2017_Season_Data.csv', index = False)


