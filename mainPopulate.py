import csv
import constants

import Topping
import populateInventory


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
 
       
#Create Inventory CSV




#Create Employee CSV



#Create Orders CSV