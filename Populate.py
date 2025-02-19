import csv
import constants
import random
import sys
import Orders
import datetime
import uuid
import os

""" This file populates five tables with constant data """


#Random var for any random values required
random.seed(10)

files = ["employees.csv", "inventory.csv", "item.csv", "orderItems.csv", "orders.csv", "toppings.csv", "orderItemToppings.csv"]
for filepath in files:
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"File '{filepath}' deleted successfully.")
    else:
        print(f"File '{filepath}' does not exist.")

### TOPPINGS ##
#Create Toppings CSV
toppingsData = [['ID', 'type', 'basePrice']]

#Input toppings data from constants
for i in range(len(constants.TOPPINGS)):
    toppingsData.append([i+1, constants.TOPPINGS[i].replace(" ", ""), constants.TOPPINGPRICES[constants.TOPPINGS[i]]])

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
        itemData.append([itemID, constants.FLAVORS[i].replace(" ",""), constants.FLAVORPRICES[constants.FLAVORS[i]], constants.MENU[constants.FLAVORS[i]][j].replace(" ", "")])
        itemID+=1

#configure csv and input data
itemCSVFilePath = 'item.csv'
with open(itemCSVFilePath, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(itemData)
print('Item data file created successfully. ' ) 


# Create Employee CSV
employeeData = [['UUID', 'isManager', 'name', 'payGrade', 'hours']]

# Add manager first
employeeData.append([constants.EMPLOYEEUUIDS[0], True, constants.MANAGER.replace(" ", ""), round(random.uniform(22.00, 28.00), 2), 8])

# Add employees from lists using indexing
for i in range(1, len(constants.EMPLOYEES)):
    employee_uuid = constants.EMPLOYEEUUIDS[i]  # Get corresponding UUID
    name = constants.EMPLOYEES[i].replace(" ", "")  # Format name
    pay_grade = round(random.uniform(13.00, 21.00), 2)
    hours = random.randint(3, 8)
    employeeData.append([employee_uuid, False, name, pay_grade, hours])

# Configure CSV and write data
employeeCSVFilePath = 'employees.csv'
with open(employeeCSVFilePath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employeeData)

print('Employee data file created successfully')


### INVENTORY ###
#Create Inventory CSV
inventoryData = [['ID', 'name', 'isAllergen', 'stockQuantity', 'unitPrice', 'cost']]

#first compile a list of all the ingredients from recipes
ingredientsList = []
for i in range(len(constants.TOPPINGS)):
    ingredientsList.append(constants.TOPPINGS[i])
for i in range(len(constants.FLAVORS)):
    for j in range(len(constants.MENU[constants.FLAVORS[i]])):
        for k in range(len(constants.ITEMSINGREDIENTS[constants.MENU[constants.FLAVORS[i]][j]])):
            ingredientsList.append(constants.ITEMSINGREDIENTS[constants.MENU[constants.FLAVORS[i]][j]][k])
ingredientsList = list(set(ingredientsList))

#input inventory data from constants 
for i in range(len(ingredientsList)):
    inventoryData.append([i+1, ingredientsList[i].replace(" ",""), constants.ALLERGENS[ingredientsList[i]], 15000, constants.MATERIALUNITPRICE[ingredientsList[i]],   round(15000*constants.MATERIALUNITPRICE[ingredientsList[i]],2)])
#configure csv and input data
inventoryCSVFilePath = 'inventory.csv'
with open(inventoryCSVFilePath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(inventoryData)
print('Inventory data file created successfully')


### ORDERS ###
def generate_random_orders():
    """Generates a dictionary of orders with randomly assigned values."""
    orders_dict = {}
    startDate = datetime.datetime(2016, 5, 28, 9) #start on harambe's death day (dihhs out for harambe)
    currentDate = startDate
    
    for i in range(364):
        peakDayFlag = False
        for peakDateString in constants.PEAKDAYS:
            peakDate = datetime.datetime.strptime(peakDateString, "%B %d, %Y")
            if ((peakDate.month == currentDate.month) and (peakDate.day == currentDate.day)):
                peakDayFlag = True

        while(True):
            if(peakDayFlag):
                delta = datetime.timedelta(minutes=random.randint(1,8), seconds=random.randint(1,24)) #these timedeltas average sales to around $1M
            else:
                delta = datetime.timedelta(minutes=random.randint(1,23), seconds=random.randint(1,53)) #these also
            currentDate += delta
            if(currentDate.hour > 18):
                break
            
            order = Orders.Orders(
                Uuid=str(uuid.uuid4()),  # Generate unique order UUID
                isFulfilled=True,  # Randomly mark as fulfilled or not
                dateTime=currentDate,  # Current timestamp
                totalPrice=0.0,                                #begin price at 0 and add at end
                customerName=random.choice(list(constants.NAMES)).replace(" ",""),  # Pick random customer name
                employeeId=random.choice(constants.EMPLOYEEUUIDS)  # Pick random employee ID
            )
            itemDict = order.generateItems()  # Generate random drinks for order
            write_orderItems_to_csv(itemDict)
            orders_dict[order.Uuid] = order.to_dict()  # Convert order to dictionary
        currentDate += datetime.timedelta(days=1)
        currentDate = currentDate.replace(hour=9, minute=0, second=0)

    return orders_dict

def write_orders_to_csv(orders_dict, filename="orders.csv"):
    """Writes orders to a CSV file using DictWriter."""
    with open(filename, mode="w", newline="") as file:
        if not orders_dict:
            print("No data to write.")
            return

        # Extract field names dynamically from first order
        fieldnames = list(next(iter(orders_dict.values())).keys())

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        # Check if 'Total Price' exists and round it
        for order in orders_dict.values():
            if "TotalPrice" in order and isinstance(order["TotalPrice"], (int, float)):
                order["TotalPrice"] = round(order["TotalPrice"], 2)

            writer.writerow(order)

    print(f"✅ CSV file '{filename}' has been created successfully.")

def write_orderItems_to_csv(itemDict, filename="orderItems.csv"):
    """Writes itemDict to a CSV file, appending if the file exists."""
    if not itemDict:
        print("No data to write.")
        return
    # Extract field names dynamically from the first item
    fieldnames = list(next(iter(itemDict.values())).keys())
    file_exists = os.path.isfile(filename)  # Check if file exists
    with open(filename, mode="a" if file_exists else "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:  
            writer.writeheader()  # Write header only if file is new
        for item in itemDict.values():
            #item["Item UUID"] = str(item["Item UUID"])
            item["subTotal"] = round(item["subTotal"], 2)  # Round Total Price

            writer.writerow(item)

    #print(f"✅ Data written to '{filename}' successfully.")

orders = generate_random_orders()  # Generate 1000 random orders
write_orders_to_csv(orders)  # Save orders to CSV