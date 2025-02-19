import csv
import constants
import random
import sys

""" This file populates five tables with coinstant data """


#Random var for any random values required
random.seed(10)

### TOPPINGS ##
#Create Toppings CSV
toppingsData = [['ID', 'type', 'basePrice']]
#Input toppings data from constants
for i in range(len(constants.TOPPINGS)):
    toppingsData.append([i+1, constants.TOPPINGS[i], constants.TOPPINGPRICES[constants.TOPPINGS[i]]])
#configure csv and input data
toppingsCSVFilePath = 'toppings.csv'
with open(toppingsCSVFilePath, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(toppingsData)
print('Toppings data file created successfully. ' )


### ITEMS ###
#Create Item CSV
itemData = [['ID', 'name', 'basePrice', 'subFlavor']]
#input item data from constants
itemID = 1
for i in range(len(constants.FLAVORS)):
    for j in range(len(constants.MENU[constants.FLAVORS[i]])):
        itemData.append([itemID, constants.FLAVORS[i], constants.FLAVORPRICES[constants.FLAVORS[i]], constants.MENU[constants.FLAVORS[i]][j]])
        itemID+=1
#configure csv and input data
itemCSVFilePath = 'item.csv'
with open(itemCSVFilePath, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(itemData)
print('Item data file created successfully. ' ) 


### EMPLOYEES ###
#Create Employee CSV
employeeData = [['ID', 'isManager', 'name', 'payGrade' ,'hours']]
#input iteam data from constants
employeeData.append([1, True, constants.MANAGER, round(constants.random.uniform(22.00, 28.00),2), 8])
for i in range(len(constants.EMPLOYEES)):
    employeeData.append([i+2, False, constants.EMPLOYEES[i], round(constants.random.uniform(13.00, 21.00), 2), constants.random.randint(3, 8)])
#configure csv and input data
employeeCSVFilePath = 'employees.csv'
with open(employeeCSVFilePath, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(employeeData)
print('Employee data file created successfully')


### INVENTORY ###
#Create Inventory CSV
inventoryData = [['ID', 'name', 'isAllergen', 'stockQuantity', 'unitPrice', 'cost']]
#first compile a list of all the ingredients from recipes
ingredientsList = []
for i in range(len(constants.FLAVORS)):
    for j in range(len(constants.MENU[constants.FLAVORS[i]])):
        for k in range(len(constants.ITEMSINGREDIENTS[constants.MENU[constants.FLAVORS[i]][j]])):
            ingredientsList.append(constants.ITEMSINGREDIENTS[constants.MENU[constants.FLAVORS[i]][j]][k])
ingredientsList = list(set(ingredientsList))
#input inventory data from constants 
for i in range(len(ingredientsList)):
    inventoryData.append([i+1, ingredientsList[i], constants.ALLERGENS[ingredientsList[i]], sys.maxsize, constants.MATERIALUNITPRICE[ingredientsList[i]],   round((sys.maxsize/1000)*constants.MATERIALUNITPRICE[ingredientsList[i]],2)])
#configure csv and input data
inventoryCSVFilePath = 'inventory.csv'
with open(inventoryCSVFilePath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(inventoryData)
print('Inventory data file created successfully')


### ORDERS ###
#Create Orders CSV
#For randomness: random employee, random item, random number of items, random toppings, random number of toppings
#keep track of the sum, making sure total sales exceeds beta million 

