# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:29:27 2020

@author: Joel
"""
import mysql.connector
import re

def remove_brackesParaQuotesComma(string):
    string = re.sub('[()]', '',string)
    string = re.sub('[\[\]]', '',string)
    string = re.sub('[\'\']', '',string)
    string = re.sub('[,]', '',string)
    return string

def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                return data

def initDB():
    arr = []
    password=file_read('pass.txt')

    password = password[0]

    config = {
        'user': 'Joel',
        'password': password,
        'host': '127.0.0.1',
        'database': 'cookingrecipes',
        'raise_on_warnings': True
        }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    arr.append(cnx)
    arr.append(cursor)
    return arr



#GET INGREDIENTS
def GetIngredientsFromRecipeName(recipeName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    recipeName = str(recipeName)
    query = "SELECT ingredient_name FROM ingredients JOIN recipe_ingredients USING(ingredientID) WHERE recipeID = (SELECT recipeID FROM recipes where recipeName = '" + recipeName + "')"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

#GET MEASUREMENT UNITS
def GetMeasurementUnitsFromRecipeName(recipeName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    recipeName = str(recipeName)
    query = "SELECT measurement_description FROM measurement_units JOIN recipe_ingredients USING(measurementID) WHERE recipeID = (SELECT recipeID FROM recipes where recipeName = '" + recipeName + "')"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

#GET MEASUREMENT QUANTITY
def GetMeasurementQtyFromRecipeName(recipeName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    recipeName = str(recipeName)
    query = "SELECT qty_amount FROM measurement_qty JOIN recipe_ingredients USING(measurement_qtyID) WHERE recipeID = (SELECT recipeID FROM recipes where recipeName = '" + recipeName + "')"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

#GET RECIPE BY NAME
def GetRecipeFromName(recipeName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    recipeName = str(recipeName)
    #GET RECIPE DESCRIPTION
    query = "SELECT description, rating FROM recipes WHERE recipeName = '" + recipeName + "'"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    
    #INGREDIENTS
    ingredients = GetIngredientsFromRecipeName(recipeName)
    results.append(ingredients)

    #MEASUREMENT QTYS
    measurementQTYs = GetMeasurementQtyFromRecipeName(recipeName)
    results.append(measurementQTYs)
    
    #MEASUREMENTS
    measurements = GetMeasurementUnitsFromRecipeName(recipeName)
    results.append(measurements)
    
    cnx.close()
    return results




#GET RECIPE NAMES FROM INGREDIENT
def GetRecipeNamesFromIngredient(ingredientName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    ingredientName = str(ingredientName)
    query = "SELECT recipeName, rating FROM recipes INNER JOIN recipe_ingredients ON recipe_ingredients.recipeID = recipes.recipeID INNER JOIN ingredients ON recipe_ingredients.ingredientID = ingredients.ingredientID WHERE ingredient_name = '" + ingredientName +"'"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

#GET RECIPE FROM INGREDINT NAME
def GetRecipeFromIngredient(ingredientName):
    results = []
    ingredientName = str(ingredientName)
    RecipeNames_andRating = GetRecipeNamesFromIngredient(ingredientName)
    
    NumOfRecipes = len(RecipeNames_andRating)
    for x in range(0,NumOfRecipes):
        tmpRecipeName = RecipeNames_andRating[x][0]
        tmpRecipeRating = RecipeNames_andRating[x][1]
        tmpRecipeName = str(tmpRecipeName)
        tmpRecipeName= remove_brackesParaQuotesComma(tmpRecipeName)
        tmpRecipe = GetRecipeFromName(tmpRecipeName)
        NameRating = (tmpRecipeName,tmpRecipeRating)
        results.append(NameRating)
        results.append(tmpRecipe)
    print("results= ",results)
    return results

#Get RECIPE NAMES WITHOUT ALLERGEN
def GetRecipeNamesWithoutAllergen(Allergen):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    Allergen = str(Allergen)
    query = "SELECT recipeName FROM recipes WHERE recipeName NOT IN (SELECT recipeName FROM recipes INNER JOIN recipe_ingredients ON recipe_ingredients.recipeID = recipes.recipeID INNER JOIN ingredients ON recipe_ingredients.ingredientID = ingredients.ingredientID WHERE ingredient_name = '" + Allergen +"')"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results



#Get Recipe without Allergen
def GetRecipeWithoutAllergen(ingredientName,Allergens):
    results = []
    allergenFreeRecipesLists = []
    allergenFreeRecipes = []
    recipesWithIng_Rating = []
    recipesWithIng = []
    recipesWithIng_Rating = GetRecipeNamesFromIngredient(ingredientName)
    
    #getting just the recipe names that have ingredient
    NumOfRecipes = len(recipesWithIng_Rating)
    for x in range(0,NumOfRecipes):
        tmpRecipeName = recipesWithIng_Rating[x][0]
        tmpRecipeName = str(tmpRecipeName)
        tmpRecipeName= remove_brackesParaQuotesComma(tmpRecipeName)
        recipesWithIng.append(tmpRecipeName)
    
    NumOfAllergens = len(Allergens)
    for x in range(0,NumOfAllergens):
        tmpAllergen = Allergens[x]
        tmpAllergenFreeRecipeNames = GetRecipeNamesWithoutAllergen(tmpAllergen)
        allergenFreeRecipesLists.append(tmpAllergenFreeRecipeNames)


    NumOfAllergenFreeLists = len(allergenFreeRecipesLists)
    firstList=allergenFreeRecipesLists[0]
    for x in range(1,NumOfAllergenFreeLists):
        tmplist=allergenFreeRecipesLists[x]
        firstList = list(set(firstList) & set(tmplist))
    #combine lists into one list of recipe names that dont include allergen
    tmplistSIZE = len(firstList)
    for x in range(0,tmplistSIZE):
        tmprecipe = firstList[x]
        tmprecipe = str(tmprecipe)
        tmprecipe = remove_brackesParaQuotesComma(tmprecipe)
        allergenFreeRecipes.append(tmprecipe)

    recipesWithIngANDAllergenFree = list(set(allergenFreeRecipes) & set(recipesWithIng))
    
    NumOfRecipes = len(recipesWithIngANDAllergenFree)
    for x in range(0,NumOfRecipes):
        tmpRecipeName = recipesWithIngANDAllergenFree[x]
        tmpRecipeName = str(tmpRecipeName)
        tmpRecipeName= remove_brackesParaQuotesComma(tmpRecipeName)
        tmpRecipe = GetRecipeFromName(tmpRecipeName)
        tmpRating = tmpRecipe[0][1]
        NameRating = (tmpRecipeName,tmpRating)
        results.append(NameRating)
        results.append(tmpRecipe)

    return results
    



#GET RECIPE NAMES FROM INGREDIENT with min rating filter
def GetRecipeNamesFromIngredient_fiterRating(ingredientName, minRating):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    ingredientName = str(ingredientName)
    minRating = str(minRating)
    query = "SELECT recipeName, rating FROM recipes INNER JOIN recipe_ingredients ON recipe_ingredients.recipeID = recipes.recipeID INNER JOIN ingredients ON recipe_ingredients.ingredientID = ingredients.ingredientID WHERE ingredient_name = '" + ingredientName +"' AND rating >= " + minRating
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

def GetRecipeFromIngredient_fiterRating(ingredientName, minRating):
    results = []
    ingredientName = str(ingredientName)
    RecipeNames_andRating = GetRecipeNamesFromIngredient_fiterRating(ingredientName, minRating)
    NumOfRecipes = len(RecipeNames_andRating)
    for x in range(0,NumOfRecipes):
        tmpRecipeName = RecipeNames_andRating[x][0]
        tmpRecipeRating = RecipeNames_andRating[x][1]
        tmpRecipeName = str(tmpRecipeName)
        tmpRecipeName= remove_brackesParaQuotesComma(tmpRecipeName)
        tmpRecipe = GetRecipeFromName(tmpRecipeName)
        NameRating = (tmpRecipeName,tmpRecipeRating)
        results.append(NameRating)
        results.append(tmpRecipe)
    return results


#get IDs for Deleting from DB
def GetIDsForDelete_byName(recipeName):
    results = []
    #get recipe ID
    ID = getRecipeID(recipeName)
    RecipeID = ID[0][0]
    
    #get ingredient ids
    Ingredient_IDS = []
    tmpINGids = getIngredientIDS(RecipeID)
    ingLength = len(tmpINGids)
    for x in range(0,ingLength):
        Ingredient_IDS.append(tmpINGids[x][0])
    
    
    #get measurement ids
    measurement_IDS = []
    tmpMeasurementIDs = getmeasurmentIDS(RecipeID)
    measurmentlength = len(tmpMeasurementIDs)
    for x in range(0,measurmentlength):
        measurement_IDS.append(tmpMeasurementIDs[x][0])
        
        
    #get measurement qty ids    
    measurement_QTYIDS = []
    tmpMeasurementQTYIDs = getmeasurmentQTYIDS(RecipeID)
    measurmentqtylength = len(tmpMeasurementQTYIDs)
    for x in range(0,measurmentqtylength):
        measurement_QTYIDS.append(tmpMeasurementQTYIDs[x][0])
    
    #results[0] = recipeID
    #results[1] = ingredientID
    #results[2] = measurementQTY ID
    #results[3] = measurementID

    
    results.append(RecipeID)
    results.append(Ingredient_IDS)
    results.append(measurement_QTYIDS)
    results.append(measurement_IDS)
    print(results)
    return results

#get recipe ID, helper function for deleting
def getRecipeID(recipeName):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    query = "SELECT recipeID FROM recipes WHERE recipeName = '" + recipeName + "'"
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results

#get ingredient IDs, helper function for deleting
def getIngredientIDS(RecipeID):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    RecipeID = str(RecipeID)
    query = "SELECT ingredientID FROM recipe_ingredients WHERE recipeID = " + RecipeID 
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results
  
#get measurement IDs, helper function for deleting
def getmeasurmentIDS(RecipeID):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    RecipeID = str(RecipeID)
    query = "SELECT measurementID FROM recipe_ingredients WHERE recipeID = " + RecipeID 
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results


#get measuremenmtQTY IDs, helper function for deleting
def getmeasurmentQTYIDS(RecipeID):
    results = []
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    RecipeID = str(RecipeID)
    query = "SELECT measurement_qtyID FROM recipe_ingredients WHERE recipeID = " + RecipeID 
    cursor.execute(query)
    myresult = cursor.fetchall()
    for x in myresult:
        results.append(x)
    cnx.close()
    return results






#A = []
#A.append("Tilapia")
#print("A= ", A)
#tmp = GetRecipeNamesWithoutAllergen("Tilapia")
#tmp = GetRecipeWithoutAllergen("chicken",A)
#tmp = GetRecipeFromIngredient("chicken")
#print("tmp =", tmp)
#tmp = GetRecipeFromName("chicken & cheese")

#tmp = GetRecipeFromIngredient("chicken")

#tmp=GetRecipeNamesFromIngredient("chicken")
#tmp=GetIngredientsFromRecipeName("chicken & cheese")
#tmp=GetMeasurementUnitsFromRecipeName("chicken & cheese")
#tmp=GetMeasurementQtyFromRecipeName("chicken & cheese")
#tmp = GetRecipeFromName("chicken & cheese")

#tmp = getRecipeID("testtest")
#print(tmp)



    