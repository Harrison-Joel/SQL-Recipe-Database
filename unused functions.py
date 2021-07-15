# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:25:12 2020

@author: Joel
"""


def searchRecipeTBL_byIngredient(ingredientName):
    results = []
    ingIDs=getIngredientID_fromingredientName(ingredientName)
   # print("ingredinet IDS: ",ingIDs)
    recipeIDs = getRecipeID_fromIngredientID(ingIDs)
    recipeNames = getRecipeName_fromRecipeID(recipeIDs)
    size = len(recipeNames)
    for x in range(0, size):
        tmpname = recipeNames[x]
        tmpname = str(tmpname)
        tmpname = remove_brackesParaQuotesComma(tmpname)
        #tmpresult = searchRecipeTBL_byName(tmpname)
        results.append(tmpname)
       # results.append(tmpresult)
    #print(results)
    return results


def getMeasurements(measurementIDS):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    size = len(measurementIDS)
    for x in range(0,size):
        tmpMeaID = measurementIDS[x]
        tmpMeaID = str(tmpMeaID)
        query ="SELECT measurement_description FROM measurement_units WHERE measurementID = " + tmpMeaID 
        cursor.execute(query)
        myresult = cursor.fetchall()
        results.append(myresult)

    cnx.close()
    return results  


def getMeasurementsQTY(measurementQTYIDS):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    size = len(measurementQTYIDS)
    for x in range(0,size):
        tmpMeaQtyID = measurementQTYIDS[x]
        tmpMeaQtyID = str(tmpMeaQtyID)
        query ="SELECT qty_amount FROM measurement_qty WHERE measurement_qtyID = " + tmpMeaQtyID 
        cursor.execute(query)
        myresult = cursor.fetchall()
        results.append(myresult)

    cnx.close()
    return results  

def getIngredients(ingredientIDS):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    size = len(ingredientIDS)
    for x in range(0,size):
        tmpINGID = ingredientIDS[x]
        tmpINGID = str(tmpINGID)
        query ="SELECT ingredient_name FROM ingredients WHERE ingredientID = " + tmpINGID 
        cursor.execute(query)
        myresult = cursor.fetchall()
        results.append(myresult)

    cnx.close()
    return results  


def getRecipeName_fromRecipeID(recipeIDs):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    size = len(recipeIDs)
    for x in range(0,size):
        tmpRecipeID = recipeIDs[x]
        tmpRecipeID = str(tmpRecipeID)
        tmpRecipeID = remove_brackesParaQuotesComma(tmpRecipeID)
        query = "SELECT recipeName FROM recipes WHERE recipeID = '" + tmpRecipeID + "'"
        cursor.execute(query)
        myresult = cursor.fetchall()
        for x in myresult:
            results.append(x)
    cnx.close()
    return results


def getRecipeID_fromIngredientID(ingredientIDs):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    size = len(ingredientIDs)
    for x in range(0,size):
        tmpINGid = ingredientIDs[x]
        tmpINGid = str(tmpINGid)    
        tmpINGid = remove_brackesParaQuotesComma(tmpINGid)
        #print("tmpINGid: ", tmpINGid)
        query = "SELECT recipeID FROM recipe_ingredients WHERE ingredientID = '" + tmpINGid + "'"
        cursor.execute(query)
        myresult = cursor.fetchall()
        for x in myresult:
            results.append(x)
    cnx.close()
    return results

def getIngredientID_fromingredientName(ingredientName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    ingredientName = str(ingredientName)
    query = "SELECT ingredientID FROM ingredients WHERE ingredient_name = '" + ingredientName + "'"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

