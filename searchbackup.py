# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:27:00 2020

@author: Joel
"""

import tkinter
import tkinter.ttk
import searchQuerys
import insertDelete
import Allergens
import re


def remove_brackesParaQuotesComma(string):
    string = re.sub('[()]', '',string)
    string = re.sub('[\[\]]', '',string)
    string = re.sub('[\'\']', '',string)
    string = re.sub('[,]', '',string)
    return string

def deleteRecipe(recipeName):
    #set IDS for recipe to be deleted
    IDs = searchQuerys.GetIDsForDelete_byName(recipeName)
    recipeID = IDs[0]
    ingredient_IDS = IDs[1]
    measurementQTY_IDS = IDs[2]
    measurement_IDS = IDs[3]

    #delete form recipe TBL
    recipeID = str(recipeID)
    insertDelete.delete_recipe_entry(recipeID)
        
    #delete ingredients
    ingSIZE = len(ingredient_IDS)
    for x in range(0,ingSIZE):
        tmpINGid = ingredient_IDS[x]
        tmpINGid = str(tmpINGid)
        insertDelete.delete_ingredientsTBL(tmpINGid)

    #deleteQTYs
    measurementQTY_SIZE = len(measurementQTY_IDS)
    for x in range(0,measurementQTY_SIZE):
        tmpQTYid = measurementQTY_IDS[x]
        tmpQTYid = str(tmpQTYid)
        insertDelete.delete_measurementQTYTBL(tmpQTYid)
    
    #delete measurement units
    measurementSIZE = len(measurement_IDS)
    for x in range(0,measurementSIZE):
        tmpMEASUREid = measurement_IDS[x]
        tmpMEASUREid = str(tmpMEASUREid)
        insertDelete.delete_measurementUnitsTBL(tmpMEASUREid)
        
    #delete recipe ingredients
    insertDelete.delete_recipeIngredientsTBL(recipeID)
    tkinter.messagebox.showinfo("delete","Recipe Deleted")
    
    return

def incrementRecipeCounter(recipes):
    global recipeCounter
    recipeSize = len(recipes)
    recipeSize=recipeSize-1
    if(recipeCounter+2 < recipeSize):
        recipeCounter = recipeCounter +2

        labelSIZE = len(Labels)
        for x in range(0,labelSIZE):
            tmplabel = Labels[x]
            tmplabel.destroy()

        display_recipe(recipes)
    else:
        tkinter.messagebox.showinfo("End of list","No more recipes")

    return

def decrementRecipeCounter(recipes):
    global recipeCounter
    if(recipeCounter-2 >= 0):
        recipeCounter = recipeCounter -2

        labelSIZE = len(Labels)
        for x in range(0,labelSIZE):
            tmplabel = Labels[x]
            tmplabel.destroy()
        display_recipe(recipes)
    else:
        tkinter.messagebox.showinfo("First recipe","No more recipes")

    return

def searchING():
    ratingInput = rating_variable.get()
    allergeninput = allergenVar.get()
    if(ratingInput == "-" and allergeninput == "-"):
        Recipes = []
        INGname = []
        INGname.append(searchINGBox)
        ingName = INGname[0].get()
        Recipes = searchQuerys.GetRecipeFromIngredient(ingName)
        display_recipe(Recipes)
    #print("recipes: ",Recipes)
    elif(ratingInput == "1" or ratingInput == "2" or ratingInput == "3" or ratingInput == "4" or ratingInput == "5"):
        Recipes = []
        INGname = []
        INGname.append(searchINGBox)
        ingName = INGname[0].get()
        Recipes = searchQuerys.GetRecipeFromIngredient_fiterRating(ingName,ratingInput)
        display_recipe(Recipes)
    elif(allergeninput != "-"):
        if(allergeninput == "Dairy"):
            Allergenlist=Allergens.CommonDairyAllergens()
        elif(allergeninput == "Nuts"):
            Allergenlist=Allergens.CommonNutAllergens()
        elif(allergeninput == "Soy"):
            Allergenlist=Allergens.CommonSoyAllergens()
        elif(allergeninput == "Wheat"):
            Allergenlist=Allergens.CommonWheatAllergens()
        elif(allergeninput == "Fish"):
            Allergenlist=Allergens.CommonFishAllergens()

        Recipes = []
        INGname = []
        INGname.append(searchINGBox)
        ingName = INGname[0].get()
        Recipes = searchQuerys.GetRecipeWithoutAllergen(ingName,Allergenlist)
        display_recipe(Recipes)
    return

def display_recipe(recipes):
    currentRecipeName = recipes[recipeCounter][0]
    currentRecipeRating = recipes[recipeCounter][1]
    currentRecipeRating = str(currentRecipeRating)
    currentRecipeName_andRating = currentRecipeName + "|| Rating: " + currentRecipeRating + "/5"
    currentRecipe =recipes[recipeCounter+1]
    ingredient_with_measurements = []
    ingLen = len(currentRecipe[1])
    for x in range(0,ingLen):
        tmp_ing = currentRecipe[1][x]
        tmp_ing= str(tmp_ing)
        tmp_ing = remove_brackesParaQuotesComma(tmp_ing)
        tmp_qty = currentRecipe[2][x]
        tmp_qty = str(tmp_qty)
        tmp_qty = remove_brackesParaQuotesComma(tmp_qty)
        tmp_mea = currentRecipe[3][x]
        tmp_mea = str(tmp_mea)
        tmp_mea = remove_brackesParaQuotesComma(tmp_mea)
        full_string = "* " + tmp_ing + " " + tmp_qty + " " + tmp_mea
        ingredient_with_measurements.append(full_string)

    recipeNameLBL = tkinter.Label(SearchRecipeWindow, text=currentRecipeName_andRating)
    recipeNameLBL.grid(column=8,row=0)
    recipeNameLBL.config(font=("Courier", 16))
    Labels.append(recipeNameLBL)

    recipeDesLBL = tkinter.Label(SearchRecipeWindow, text=currentRecipe[0][0])
    recipeDesLBL.grid(column=8,row=2)
    recipeDesLBL.config(font=("Courier", 12))
    Labels.append(recipeDesLBL)

    #print ing
    ingLen = len(ingredient_with_measurements)
    curRow = 2
    for x in range(0,ingLen):
        curRow = curRow+2
        ingLBL = tkinter.Label(SearchRecipeWindow, text=ingredient_with_measurements[x])
        ingLBL.grid(column=8,row=curRow)
        ingLBL.config(font=("Courier", 12))
        Labels.append(ingLBL)

   
    lengthofrecipe = len(recipes)
    if(lengthofrecipe > 2):
         nextBTN = tkinter.Button(SearchRecipeWindow, text="next recipe", command=lambda: incrementRecipeCounter(recipes))
         nextBTN.grid(column=12, row=8)
    if(recipeCounter > 1):
        prevBTN = tkinter.Button(SearchRecipeWindow, text="previous recipe", command=lambda: decrementRecipeCounter(recipes))
        prevBTN.grid(column=10, row=8)
    btn4 = tkinter.Button(SearchRecipeWindow, text="delete", command= lambda: deleteRecipe(currentRecipeName))
    btn4.grid(column=10, row=6)
    return

def searchRecipe():
    recipe = []
    RecipeName.append(searchRecipeBox)
    recipeName = RecipeName[0].get()
    recipe = searchQuerys.GetRecipeFromName(recipeName)
    print(recipe[0])
    #print(recipe[1])
    #build ingredients list
    ingredient_with_measurements = []
    ingLen = len(recipe[1])
    for x in range(0,ingLen):
        tmp_ing = recipe[1][x]
        tmp_ing= str(tmp_ing)
        tmp_ing = remove_brackesParaQuotesComma(tmp_ing)
        tmp_qty = recipe[2][x]
        tmp_qty = str(tmp_qty)
        tmp_qty = remove_brackesParaQuotesComma(tmp_qty)
        tmp_mea = recipe[3][x]
        tmp_mea = str(tmp_mea)
        tmp_mea = remove_brackesParaQuotesComma(tmp_mea)
        full_string = "* " + tmp_ing + " " + tmp_qty + " " + tmp_mea
        ingredient_with_measurements.append(full_string)
    
    currentRecipeRating = recipe[0][1]
    currentRecipeRating= str(currentRecipeRating)
    recipeName = recipeName + "|| Rating: " + currentRecipeRating + "/5"
    recipeNameLBL = tkinter.Label(SearchRecipeWindow, text=recipeName)
    recipeNameLBL.grid(column=8,row=0)
    recipeNameLBL.config(font=("Courier", 16))
    
    recipeDesLBL = tkinter.Label(SearchRecipeWindow, text=recipe[0][0])
    recipeDesLBL.grid(column=8,row=2)
    recipeDesLBL.config(font=("Courier", 12))
    
    #print ing
    ingLen = len(ingredient_with_measurements)
    curRow = 2
    for x in range(0,ingLen):
        curRow = curRow+2
        ingLBL = tkinter.Label(SearchRecipeWindow, text=ingredient_with_measurements[x])
        ingLBL.grid(column=8,row=curRow)
        ingLBL.config(font=("Courier", 12))
    btn4 = tkinter.Button(SearchRecipeWindow, text="delete", command= lambda: deleteRecipe(recipeName))
    btn4.grid(column=10, row=6)
    
    return


exec(open("./insertDelete.py").read())

exec(open("./searchQuerys.py").read())

SearchRecipeWindow = tkinter.Tk()
SearchRecipeWindow.title("Search Recipes")
SearchRecipeWindow.iconbitmap(r'C:\Users\Joel\Desktop\DataBase project\icon.ico')
SearchRecipeWindow.geometry('1000x600')

RecipeName = []
INGname = []
recipeCounter = 0
Labels = []

rating_variable = tkinter.StringVar(SearchRecipeWindow)
rating_variable.set("-") # default value

allergenVar = tkinter.StringVar(SearchRecipeWindow)
allergenVar.set("-") # default value


tkinter.ttk.Separator(SearchRecipeWindow, orient=tkinter.VERTICAL).grid(column=7, row=0, rowspan=8, sticky='ns')
tkinter.ttk.Separator(SearchRecipeWindow, orient=tkinter.HORIZONTAL).grid(column=0, row=7, columnspan=5, sticky='ew')






lbl1 = tkinter.Label(SearchRecipeWindow, text="Recipe name:")
lbl1.grid(column=0,row=0)

lbl2 = tkinter.Label(SearchRecipeWindow, text="Ingredient name:")
lbl2.grid(column=0,row=4)

searchRecipeBox = tkinter.Entry(SearchRecipeWindow,width=20)
searchRecipeBox.grid(column=0, row=2)

searchINGBox = tkinter.Entry(SearchRecipeWindow,width=20)
searchINGBox.grid(column=0, row=6)

searchBTN = tkinter.Button(SearchRecipeWindow, text="Search", command=searchRecipe)
searchBTN.grid(column=5, row=2)
searchBTNing = tkinter.Button(SearchRecipeWindow, text="Search", command=searchING)
searchBTNing.grid(column=5, row=6)

filterLBL = tkinter.Label(SearchRecipeWindow, text="Filter Options:")
filterLBL.grid(column=0,row=10)
filterLBL.config(font=(14))

ratingLBL = tkinter.Label(SearchRecipeWindow, text="Minimum rating:")
ratingLBL.grid(column=0,row=12)
#drop down menu for rating
ratingEntry = tkinter.OptionMenu(SearchRecipeWindow, rating_variable, "-", "1", "2", "3","4","5")
ratingEntry.grid(column=2, row=12)


allergenLBL = tkinter.Label(SearchRecipeWindow, text="Allergen:")
allergenLBL.grid(column=0,row=14)
#drop down menu for rating
ratingEntry = tkinter.OptionMenu(SearchRecipeWindow, allergenVar, "-", "Dairy", "Nuts", "Soy","Wheat","Fish")
ratingEntry.grid(column=2, row=14)


SearchRecipeWindow.mainloop()