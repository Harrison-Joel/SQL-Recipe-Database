# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:48:47 2020

@author: Joel
"""
import mysql.connector


def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                return data
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


def insert_into_recipeTBL(recipeIDin, recipeNamein, descriptionin, ratingin):
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    ratingin = str(ratingin)
    query = "INSERT INTO recipes (recipeID, recipeName, description, rating) VALUES (" + recipeIDin + ", '" + recipeNamein + "', '" + descriptionin + "', " + ratingin + ")"
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return

def insert_into_recipeIngredientsTBL(recipeID, ingredientID, measurementID, measurementQTYID):
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    query = "INSERT INTO recipe_ingredients (recipeID, ingredientID, measurementID, measurement_qtyID) VALUES (" + recipeID + ", " + ingredientID + ", " + measurementID + ", " + measurementQTYID + ")"
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return

def insert_into_measurementUnitsTBL(measurementID,measurementdes):
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    query = "INSERT INTO measurement_units (measurementID, measurement_description) VALUES (" + measurementID + ", '" + measurementdes + "')"
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return

def insert_into_measurementQTYTBL(measurementQTYID,QTYamount):
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    query = "INSERT INTO measurement_qty (measurement_qtyID, qty_amount) VALUES (" + measurementQTYID + ", '" + QTYamount + "')"
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return

def insert_into_ingredientsTBL(ingredientID,ingredientName):
    arr = initDB()
    cnx = arr[0]
    cursor = arr[1]
    query = "INSERT INTO ingredients (ingredientID, ingredient_name) VALUES (" + ingredientID + ", '" + ingredientName + "')"
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return

def delete_ingredientsTBL(ingredientID):
    query = "DELETE FROM ingredients WHERE ingredientID = " + ingredientID
    cursor.execute(query)
    cnx.commit()
    return

def delete_measurementQTYTBL(measurementQTYID):
    query = "DELETE FROM measurement_qty WHERE measurement_qtyID = " + measurementQTYID
    cursor.execute(query)
    cnx.commit()
    return

def delete_measurementUnitsTBL(measurementID):
    query = "DELETE FROM measurement_units WHERE measurementID = " + measurementID
    cursor.execute(query)
    cnx.commit()
    return

def delete_recipeIngredientsTBL(recipeID):
    query = "DELETE FROM recipe_ingredients WHERE recipeID = " + recipeID
    cursor.execute(query)
    cnx.commit()
    return

def delete_recipe_entry(recipeID):
    query = "DELETE FROM recipes WHERE recipeID = " + recipeID
    cursor.execute(query)
    cnx.commit()
    return

#insert statment
#sql = "INSERT INTO recipes (recipeID, recipeName, description) VALUES (1001, 'testPython3', 'ymmm its good')"

#insert_into_recipeTBL("102","testPYfunction", "example desctiption", "4")
#insert_into_recipeIngredientsTBL("1","2","2","2",mycursor)
#insert_into_measurementUnitsTBL("1","cups",mycursor)
#insert_into_measurementQTYTBL("1","2/3", mycursor)
#insert_into_ingredientsTBL("1","chicken",mycursor)

#delete_ingredientsTBL("1",mycursor)
#delete_measurementQTYTBL("1",mycursor)
#delete_measurementUnitsTBL("1",mycursor)
#delete_recipeIngredientsTBL("1",mycursor)
#delete_recipe_entry("102",mycursor)



