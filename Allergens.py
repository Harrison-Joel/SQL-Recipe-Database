# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:10:51 2020

@author: Joel
"""

def CommonDairyAllergens():
    DairyAllergens = []
    file1 = open('Dairy.txt', 'r') 
    Lines = file1.readlines() 
  
    # Strips the newline character 
    for line in Lines: 
        DairyAllergens.append(line.strip())
        #print("{}".format(line.strip())) 
    #print(DairyAllergens)
    return DairyAllergens
 
def CommonNutAllergens():
    NutAllergens = []
    file1 = open('Nuts.txt', 'r') 
    Lines = file1.readlines() 
  
    # Strips the newline character 
    for line in Lines: 
        NutAllergens.append(line.strip())
        #print("{}".format(line.strip())) 
    #print(NutAllergens)
    return NutAllergens


def CommonSoyAllergens():
    SoyAllergens = []
    file1 = open('Soy.txt', 'r') 
    Lines = file1.readlines() 
  
    # Strips the newline character 
    for line in Lines: 
        SoyAllergens.append(line.strip())
        #print("{}".format(line.strip())) 
    #print(NutAllergens)
    return SoyAllergens

def CommonWheatAllergens():
    WheatAllergens = []
    file1 = open('Wheat.txt', 'r') 
    Lines = file1.readlines() 
  
    # Strips the newline character 
    for line in Lines: 
        WheatAllergens.append(line.strip())
        #print("{}".format(line.strip())) 
    #print(NutAllergens)
    return WheatAllergens

def CommonFishAllergens():
    FishAllergens = []
    file1 = open('Fish.txt', 'r') 
    Lines = file1.readlines() 
  
    # Strips the newline character 
    for line in Lines: 
        FishAllergens.append(line.strip())
        #print("{}".format(line.strip())) 
    #print(NutAllergens)
    return FishAllergens


#testing statments

#tmp=CommonFishAllergens()
#CommonWheatAllergens()
#print(tmp)
#CommonSoyAllergens()
#CommonNutAllergens()
#CommonDairyAllergens()