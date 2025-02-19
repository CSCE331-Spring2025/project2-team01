import csv
import constants  # Ensure ITEMSINGREDIENTS is in constants.py

# File paths
itemDataCSV = "item.csv"
inventoryDataCSV = "inventory.csv"
outputCSV = "itemIngredient.csv"

# Read itemData.csv
itemData = []
with open(itemDataCSV, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    for row in reader:
        itemData.append(row)

# Read inventoryData.csv
inventoryData = []
with open(inventoryDataCSV, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    inventoryHeader = next(reader)  # Skip header row
    for row in reader:
        inventoryData.append(row)

# Create a lookup dictionary for inventory item names -> IDs
inventoryLookup = {row[1]: row[0] for row in inventoryData}  # {name: ID}

itemIngredientData = [['ID', 'drinkFlavorId', 'InventoryId', 'Quantity']]
itemIngrId = 1

# Process each item in itemData
for item in itemData:
    item_id = item[0]  # The unique ID of the item
    item_name = item[3].replace(" ", "")  # Normalize the subFlavor name

    # Get ingredients list from ITEMSINGREDIENTS
    ingredients = constants.ITEMSINGREDIENTS.get(item_name, [])

    for ingredient in ingredients:
        # Find the inventory ID for the ingredient
        inventory_id = inventoryLookup.get(ingredient)

        if inventory_id:
            itemIngredientData.append([itemIngrId, item_id, inventory_id, 1])
            itemIngrId += 1
        else:
            print(f"⚠️ Warning: Ingredient '{ingredient}' not found in inventory")

# Write the processed data to itemIngredient.csv
with open(outputCSV, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(itemIngredientData)

print("✅ Item Ingredients data file created successfully.")
