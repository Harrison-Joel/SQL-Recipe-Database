# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:28:21 2020

@author: Joel
"""

import tkinter
import random
import insertDelete



exec(open("./insertDelete.py").read())


def grid_hide(widget):
    #print("hide called")
    widget._grid_info = widget.grid_info()
    widget.grid_remove()

def grid_show(widget):
    widget.grid(**widget._grid_info)

addRecipeWindow = tkinter.Tk()
addRecipeWindow.title("Add a recipe")
addRecipeWindow.iconbitmap(r'C:\Users\Joel\Desktop\DataBase project\icon.ico')
addRecipeWindow.geometry('1000x600')


lbl1 = tkinter.Label(addRecipeWindow, text="")



all_entries = []
all_entries_amountqty = []
all_entries_amountsize = []
dir_entries = []
RecipeName = []

rating_variable = tkinter.StringVar(addRecipeWindow)
rating_variable.set("1") # default value

def add_txt_entry():
    #print("add txt called")
    rownum = len(all_entries) + 3
    txttmp = tkinter.Entry(addRecipeWindow,width=20)
    txttmp.grid(column=0, row=rownum)
    txttmp_amountqty = tkinter.Entry(addRecipeWindow,width=10)
    txttmp_amountqty.grid(column=2, row=rownum)
    txttmp_amountsize = tkinter.Entry(addRecipeWindow,width=10)
    txttmp_amountsize.grid(column=4, row=rownum)
    all_entries_amountsize.append(txttmp_amountsize)
    all_entries.append(txttmp)
    all_entries_amountqty.append(txttmp_amountqty)

    
    
#def add_dir_entry():
    #rownum = len(dir_entries) + 3
    #txttmp = tkinter.Entry(addRecipeWindow,width=40)
    #txttmp.grid(column=8, row=rownum)
    #dir_entries.append(txttmp)
    
def submit():
    #number of mesurement units
    size_amountsize = len(all_entries_amountsize)
    
    #array of mesurement unit ids
    measurementID_array = []
    for x in range(0,size_amountsize):
        measurementID = random.randint(1,100000000)
        measurementID = str(measurementID)
        measurementID_array.append(measurementID)
            
    #array for each measurment qty ids
    size_amountqty = len(all_entries_amountqty)
    measurementQtyID_array = []
    for x in range(0,size_amountqty):
        measurementQtyID = random.randint(1,100000000)
        measurementQtyID = str(measurementQtyID)
        measurementQtyID_array.append(measurementQtyID)
        
   #array for ingredient ids  
    ingredientID_array = []
    size = len(all_entries)
    for x in range(0,size):
        ingredientID = random.randint(1,100000000)
        ingredientID = str(ingredientID)
        ingredientID_array.append(ingredientID)
        
    #recipe ID    
    recipeID = random.randint(1,100000000)
    recipeID = str(recipeID)

    

    #print("1. ",recipeID,"2. ", measurementID, "3. ",measurementQtyID, "4. ", ingredientID )
    
    #RECIPE
    recipeName = RecipeName[0].get()
    print(recipeName)
    recipeDes = dir_entries[0].get()
    print(recipeDes)
    ratingInput = rating_variable.get()
    #insert into recipes tbl
    insertDelete.insert_into_recipeTBL(recipeID,recipeName,recipeDes,ratingInput)
    
    #insert into recipe ingredients tbl
    for x in range(0,size):
        ingredientID = ingredientID_array[x]
        measurementID = measurementID_array[x]
        measurementQtyID = measurementQtyID_array[x]
        insertDelete.insert_into_recipeIngredientsTBL(recipeID,ingredientID,measurementID,measurementQtyID)
 
    
    for x in range(0,size_amountsize):
        tmp=all_entries_amountsize[x].get()
        measurementID = measurementID_array[x]
        insertDelete.insert_into_measurementUnitsTBL(measurementID,tmp)
      
    for x in range(0,size_amountqty):
        tmp=all_entries_amountqty[x].get()
        measurementQtyID = measurementQtyID_array[x]
        insertDelete.insert_into_measurementQTYTBL(measurementQtyID,tmp)
        
    for x in range(0,size):
       tmp = all_entries[x].get()
       ingredientID = ingredientID_array[x]
       insertDelete.insert_into_ingredientsTBL(ingredientID,tmp)
       

    tkinter.messagebox.showinfo("Submitted","Reciped added")



        
def Manual_recipe_input():
    #labels 
    lbl1 = tkinter.Label(addRecipeWindow, text="Ingredients:")
    lbl1.grid(column=0,row=0)
    measurementQTY = tkinter.Label(addRecipeWindow, text="measurement QTY:")
    measurementQTY.grid(column=2,row=0)
    measurement = tkinter.Label(addRecipeWindow, text="measurement:")
    measurement.grid(column=4,row=0)
    Recipe_name = tkinter.Label(addRecipeWindow, text="Recipe name")
    Recipe_name.grid(column=6,row=0)
    Directions_lbl = tkinter.Label(addRecipeWindow, text="Description:")
    Directions_lbl.grid(column=8,row=0)
    rating_lbl = tkinter.Label(addRecipeWindow, text="Rating:")
    rating_lbl.grid(column=10,row=0)

    #entrys
    ingredient1 = tkinter.Entry(addRecipeWindow,width=20)
    ingredient1.grid(column=0, row=3)
    amountQty = tkinter.Entry(addRecipeWindow,width=10)
    amountQty.grid(column=2, row=3)
    amountSize = tkinter.Entry(addRecipeWindow,width=10)
    amountSize.grid(column=4, row=3)
    Name_entry = tkinter.Entry(addRecipeWindow,width=20)
    Name_entry.grid(column=6, row=3)
    Directions1 = tkinter.Entry(addRecipeWindow,width=40)
    Directions1.grid(column=8, row=3)
    
    #drop down menu for rating
    ratingEntry = tkinter.OptionMenu(addRecipeWindow, rating_variable, "1", "2", "3","4","5")
    ratingEntry.grid(column=10, row=3)
    
    #add entrys to array variables to use when calling insert
    all_entries.append(ingredient1)
    all_entries_amountqty.append(amountQty)
    all_entries_amountsize.append(amountSize)
    dir_entries.append(Directions1)
    RecipeName.append(Name_entry)
    #print(len(all_entries))
    btn3 = tkinter.Button(addRecipeWindow, text="add ingredient", command=add_txt_entry)
    btn3.grid(column=5, row=0)
    btn4 = tkinter.Button(addRecipeWindow, text="done", command=submit)
    btn4.grid(column=5, row=6)
    #dir_btn = tkinter.Button(addRecipeWindow, text="add direction", command=add_dir_entry)
    #dir_btn.grid(column=5, row=3)

    
def upload_recipe_input():
    tkinter.messagebox.showinfo("upload","Not implemented yet")

def Button1():
    btn1["state"] = tkinter.DISABLED
    btn2["state"] = tkinter.NORMAL
    btn1.place(x=900, y=0)
    btn2.place(x=950, y=0)
    Manual_recipe_input()
    
def Button2():
    btn2["state"] = tkinter.DISABLED
    btn1["state"] = tkinter.NORMAL
    btn1.place(x=900, y=0)
    btn2.place(x=950, y=0)
    upload_recipe_input()
    
btn1 = tkinter.Button(addRecipeWindow, text="Manual", command=Button1)

btn1.grid(column=2, row=0)

btn2 = tkinter.Button(addRecipeWindow, text="Upload", command=Button2)

btn2.grid(column=3, row=0)

addRecipeWindow.mainloop()