import csv
import os
import random
import constants  # Ensure ITEMSINGREDIENTS is in constants.py

# File paths
itemDataCSV = "item.csv"
inventoryDataCSV = "inventory.csv"
orderItemsCSV = "orderItems.csv"
outputItemIngredientCSV = "itemIngredient.csv"
outputOrderMaterialsCSV = "orderMaterials.csv"

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
with open(outputItemIngredientCSV, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(itemIngredientData)

print("✅ Item Ingredients data file created successfully.")


def write_orderMaterials_to_csv(filename=outputOrderMaterialsCSV):
    """Writes order materials data to orderMaterials.csv based on orderItems.csv and inventory.csv."""

    # Ensure required files exist
    if not os.path.exists(orderItemsCSV) or not os.path.exists(inventoryDataCSV):
        print("❌ Error: Missing orderItems.csv or inventory.csv. Cannot generate orderMaterials.")
        return

    # Read orderItems.csv to get orderId values (each row represents a drink)
    with open(orderItemsCSV, mode="r") as file:
        reader = csv.DictReader(file)
        orderItems = [row for row in reader]  # Get all order items

    # Read inventory.csv and store material inventory IDs
    inventory_dict = {}
    with open(inventoryDataCSV, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"] in ["Cup", "Lid", "Straw", "Napkin"]:
                inventory_dict[row["name"]] = row["ID"]  # Store material name → inventory ID mapping

    orderMaterialsData = []
    materialIdCounter = 1
    napkinCount = {}  # Track napkin count per orderId to avoid duplicates

    for item in orderItems:
        orderID = item["orderId"]  # Get orderId from orderItem.csv

        # Assign 1 unit for Cup, Lid, and Straw per drink
        for materialName in ["Cup", "Lid", "Straw"]:
            inventoryID = inventory_dict.get(materialName, None)
            if inventoryID:
                orderMaterialsData.append([materialIdCounter, orderID, materialName, inventoryID, 1])
                materialIdCounter += 1
        # Assign a random quantity (1-3) for Napkins per order (not per drink)
        if orderID not in napkinCount:
            inventoryID = inventory_dict.get("Napkin", None)
            if inventoryID:
                napkin_quantity = random.randint(1, 3)  # Random napkin quantity
                orderMaterialsData.append([materialIdCounter, orderID, "Napkin", inventoryID, napkin_quantity])
                napkinCount[orderID] = True  # Ensure only one napkin entry per orderId
                materialIdCounter += 1
    # Write data to orderMaterials.csv
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["orderMaterialID", "orderId", "name", "inventoryId", "quantity"])  # Write header
        writer.writerows(orderMaterialsData)

    print(f"✅ {filename} generated successfully.")

# Generate orderMaterials.csv
write_orderMaterials_to_csv()
