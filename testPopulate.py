import csv
import random
import uuid
from datetime import datetime

# Constants
flavors = {
    "Brewed Tea": ["Classic black", "Classic green", "Classic oolong", "Honey black", "Honey Green", "Honey oolong", "Ginger", "Wintermelon"],
    "Milk Tea": ["Honey milk black", "Honey milk green", "Honey oolong", "Mango ginger milk", "Coffee milk", "Thai milk", "Classic", "Taro", "Okinawa milk", "Matcha milk", "Hokkaido", "Ginger milk", "QQ happy family", "Classic coffee"],
    "Fruit Tea": ["Hawaii fruit tea", "Honey lemonade", "Kiwi fruit tea", "Passion fruit orange and grapefruit", "Strawberry", "Tropical fruit", "Mango and passion fruit", "Peach kiwi", "Peach", "Wintermelon lemonade", "Mango green"],
    "Fresh Milk": ["Fresh milk black tea", "Fresh milk green tea", "Fresh milk oolong tea", "Wintermelon with fresh milk", "Cocoa lover with fresh milk", "Matcha with fresh milk", "fresh milk family", "Handmade taro with fresh milk"],
    "Ice Blended": ["Milk tea ice blended", "Peach tea ice blended", "Thai tea ice blended", "Taro ice blended", "Strawberry ice blended", "Oreo ice blended", "Coffee ice blended", "Mango ice blended", "Matcha ice blended"],
    "Tea Mojito": ["Lime mojito", "Strawberry mojito", "Mango mojito", "Peach mojito"]
}

toppings = ["Pearl", "Crystal boba", "Mini pearl", "Lychee jelly", "Pudding", "Aloe vera", "Herb jelly", "Crema", "Aiyu jelly", "Ice cream", "Honey pack", "Edible green"]

materials = {
    "Cups": [12, 16, 24],  # sizes in oz
    "Lids": 0.10,
    "Straws": 0.05,
    "Cup Holders": 0.10,
    "Spoons": 0.05,
    "Napkins": 0.03,
    "Drink Sleeves": 0.10
}

# Helper Functions
def random_name():
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Chris", "Riley", "Casey", "Jamie"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
    return random.choice(first_names) + " " + random.choice(last_names)

def random_flavor():
    drink_category = random.choice(list(flavors.keys()))
    drink = random.choice(flavors[drink_category])
    return drink_category, drink

def random_topping():
    return random.choice(toppings)

def random_quantity():
    return random.randint(1, 20)

def calculate_order_cost(num_drinks, num_toppings):
    total_cost = 0
    for _ in range(num_drinks):
        drink_category, drink = random_flavor()
        if "Brewed Tea" in drink_category:
            total_cost += 4.25
        elif "Milk Tea" in drink_category:
            total_cost += 4.75
        elif "Fruit Tea" in drink_category:
            total_cost += 5.75
        elif "Fresh Milk" in drink_category:
            total_cost += 4.75
        elif "Ice Blended" in drink_category:
            total_cost += 6.00
        elif "Tea Mojito" in drink_category:
            total_cost += 6.00
        # Add topping cost
        total_cost += num_toppings * 0.75
    return total_cost

# Generate CSV Data
order_data = []
for _ in range(100):  # Generate 100 random orders
    order_id = str(uuid.uuid4())  # Random UUID for each order
    customer_name = random_name()
    num_drinks = random.randint(1, 6)
    num_toppings = random.randint(1, 3)
    
    order_cost = calculate_order_cost(num_drinks, num_toppings)
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add order to data list
    order_data.append([order_id, customer_name, num_drinks, num_toppings, order_cost, date_time])

# Write to CSV file
with open('orders.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Order ID", "Customer Name", "Number of Drinks", "Number of Toppings", "Total Cost", "Date"])
    writer.writerows(order_data)

print("CSV file 'orders.csv' has been generated.")