# -*- coding: utf-8 -*-

import tkinter
#from importlib import reload  
import tkinter.ttk
import addRecipe
import searchRecipe


window = tkinter.Tk()

window.title("Cooking Recipe Portal")
window.iconbitmap(r'C:\Users\Joel\Desktop\DataBase project\icon.ico')
window.geometry('300x160')




def Button1():
    addRecipe.addRecipeRunAll()
    
    return


def Button2():
    searchRecipe.searchRecipeRunAll()
    return
    
btn = tkinter.Button(window, text="Add Recipe", command=Button1)
btn.grid(column=2, row=0)
btn.config( height = 10, width = 20 )

btn2 = tkinter.Button(window, text="Search Recipe", command=Button2)
btn2.grid(column=4, row=0)
btn2.config( height = 10, width = 20 )

window.mainloop()