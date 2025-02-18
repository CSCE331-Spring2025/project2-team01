import random

random.seed(10)

MENU = {
    "Brewed tea": [
        "Classic black",
        "Classic green",
        "Classic oolong",
        "Honey black",
        "Honey green",
        "Honey oolong",
        "Ginger",
        "Wintermelon"
    ],
    "Milk tea": [
        "Honey milk black",
        "Honey milk green",
        "Honey oolong",
        "Mango ginger milk",
        "Coffee milk",
        "Thai milk",
        "Classic",
        "Taro",
        "Okinawa milk",
        "Matcha milk",
        "Hokkaido",
        "Ginger milk",
        "QQ happy family",
        "Classic coffee"
    ],
    "Fruit tea": [
        "Hawaii fruit tea",
        "Honey lemonade",
        "Kiwi fruit tea",
        "Passion fruit orange and grapefruit",
        "Strawberry",
        "Tropical fruit",
        "Mango and passion fruit",
        "Peach kiwi",
        "Peach",
        "Wintermelon lemonade",
        "Mango green"
    ],
    "Fresh milk": [
        "Fresh milk black tea",
        "Fresh milk green tea",
        "Fresh milk oolong tea",
        "Wintermelon with fresh milk",
        "Cocoa lover with fresh milk",
        "Matcha with fresh milk",
        "Fresh milk family",
        "Handmade taro with fresh milk"
    ],
    "Ice blended": [
        "Milk tea ice blended",
        "Peach tea ice blended",
        "Thai tea ice blended",
        "Taro ice blended",
        "Strawberry ice blended",
        "Oreo ice blended",
        "Coffee ice blended",
        "Mango ice blended",
        "Matcha ice blended"
    ],
    "Tea mojito": [
        "Lime mojito",
        "Strawberry mojito",
        "Mango mojito",
        "Peach mojito"
    ]
}

MONTHDAYS = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

TOPPINGS = [
    "Pearl",
    "Crystal boba",
    "Mini pearl",
    "Lychee jelly",
    "Pudding",
    "Aloe vera",
    "Herb jelly",
    "Crema",
    "Aiyu jelly",
    "Ice cream",
    "Honey pack",
    "Edible green"
]

ITEMSINGREDIENTS = {
    "Classic black": ["Black tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Classic green": ["Green tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Classic oolong": ["Oolong tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey black": ["Black tea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey green": ["Green tea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey oolong": ["Oolong tea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Ginger": ["Ginger", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Wintermelon": ["Wintermelon", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey milk black": ["Black tea", "Honey", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey milk green": ["Green tea", "Honey", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey oolong": ["Oolong tea", "Honey", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Mango ginger milk": ["Mango", "Ginger", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Coffee milk": ["Coffee", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Thai milk": ["Thai tea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Classic": ["Black tea", "Sugar", "Water", "Milk", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Taro": ["Taro", "Sugar", "Milk", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Okinawa milk": ["Okinawa brown sugar", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Matcha milk": ["Matcha", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Hokkaido": ["Hokkaido milk", "Sugar", "Water", "Milk", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Ginger milk": ["Ginger", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "QQ happy family": ["Tapioca pearls", "Herb jelly", "Lychee jelly", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Classic coffee": ["Coffee", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Hawaii fruit tea": ["Pineapple", "Mango", "Lemon", "Tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Honey lemonade": ["Honey", "Lemon", "Water", "Sugar", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Kiwi fruit tea": ["Kiwi", "Tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Passion fruit orange and grapefruit": ["Passion fruit", "Orange", "Grapefruit", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Strawberry": ["Strawberry", "Sugar", "Water", "Ice", "Lemon", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Tropical fruit": ["Mango", "Pineapple", "Papaya", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Mango and passion fruit": ["Mango", "Passion fruit", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Peach kiwi": ["Peach", "Kiwi", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Peach": ["Peach", "Sugar", "Water", "Ice", "Lemon", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Wintermelon lemonade": ["Wintermelon", "Lemon", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Mango green": ["Mango", "Green tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Fresh milk black tea": ["Black tea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Fresh milk green tea": ["Green tea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Fresh milk oolong tea": ["Oolong tea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Wintermelon with fresh milk": ["Wintermelon", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Cocoa lover with fresh milk": ["Cocoa", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Matcha with fresh milk": ["Matcha", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Fresh milk family": ["Milk", "Sugar", "Water", "Ice", "Tapioca pearls", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Handmade taro with fresh milk": ["Taro", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Milk tea ice blended": ["Milk tea", "Ice", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Peach tea ice blended": ["Peach tea", "Ice", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Thai tea ice blended": ["Thai tea", "Ice", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Taro ice blended": ["Taro", "Ice", "Sugar", "Water", "Milk", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Strawberry ice blended": ["Strawberry", "Ice", "Sugar", "Water", "Milk", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Oreo ice blended": ["Oreo", "Ice", "Milk", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Coffee ice blended": ["Coffee", "Ice", "Milk", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Mango ice blended": ["Mango", "Ice", "Sugar", "Water", "Milk", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Matcha ice blended": ["Matcha", "Ice", "Milk", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Lime mojito": ["Lime", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Strawberry mojito": ["Strawberry", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Mango mojito": ["Mango", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
    "Peach mojito": ["Peach", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"]
}

FLAVORPRICES = {
    "Brewed tea": 4.25,
    "Milk tea": 4.75,
    "Fruit tea": 5.75,
    "Fresh milk": 4.75,
    "Ice blended": 6.00,
    "Tea mojito": 6.00
}

PEAKDAYS = [
    "March 16, 2024",
    "March 17, 2024",
    "April 20, 2024",
    "May 4, 2024",
    "May 11, 2024",
    "May 12, 2024",
    "August 18, 2024",
    "August 25, 2024",
    "October 12, 2024",
    "October 13, 2024",
    "November 25, 2024",
    "November 26, 2024",
    "November 27, 2024",
    "December 5, 2024",
    "December 8, 2024",
    "December 9, 2024",
    "December 10, 2024",
    "December 11, 2024",
    "December 12, 2024",
    "December 13, 2024",
    "January 17, 2025",
    "March 13, 2025",
    "March 14, 2025",
    "March 15, 2025",
    "March 16, 2025",
    "March 17, 2025",
    "April 21, 2025",
    "May 2, 2025",
    "May 4, 2025",
    "May 5, 2025",
    "May 6, 2025",
    "May 7, 2025",
    "May 8, 2025",
    "May 9, 2025",
    "May 11, 2025",
    "May 12, 2025",
    "May 13, 2025"
]

TOPPINGPRICES = {
    "Pearl": 0.50,
    "Crystal boba": 0.60,
    "Mini pearl": 0.50,
    "Lychee jelly": 0.75,
    "Pudding": 0.70,
    "Aloe vera": 0.65,
    "Herb jelly": 0.55,
    "Crema": 0.80,
    "Aiyu jelly": 0.70,
    "Ice cream": 1.50,
    "Honey pack": 0.40,
    "Edible green": 0.60
}

FLAVORS = [
    "Brewed tea",
    "Milk tea",
    "Fruit tea",
    "Fresh milk",
    "Ice blended",
    "Tea mojito"
]

MANAGER = 'Queen Rev'

EMPLOYEES = ['Paul Taele', 
             'Philip Ritchey', 
             'Aakash Tyagi', 
             'Teresa Leyk', 
             'Sandeep Kumar', 
             'David Kebo', 
             'Tim Davis',
             'Riccardo Bettati',
             'Hyunyoung Lee', 
             'Michael Moore'
             ]

ALLERGENS = {
    'Hokkaido milk': True,
    'Lime': False,
    'Lemon': False,
    'Sugar': False,
    'Drink sleeve': False,
    'Oolong tea': False,
    'Taro': False,
    'Tea': False,
    'Lid': False,
    'Tapioca pearls': False,
    'Strawberry': False,
    'Milk tea': True,
    'Matcha': False,
    'Honey': False,
    'Lychee jelly': False,
    'Wintermelon': False,
    'Peach tea': False,
    'Peach': False,
    'Ice': False,
    'Napkin': False,
    'Grapefruit': False,
    'Passion fruit': False,
    'Ginger': False,
    'Orange': False,
    'Straw': False,
    'Black tea': False,
    'Cup': False,
    'Cocoa': True,
    'Kiwi': True,
    'Water': False,
    'Coffee': False,
    'Oreo': True,
    'Okinawa brown sugar': False,
    'Milk': True,
    'Thai tea': True,
    'Papaya': False,
    'Green tea': False,
    'Mango': False,
    'Herb jelly': False,
    'Pineapple': False,
    'Mint': False
}

MATERIALUNITPRICE = {
    'Hokkaido milk': 3.50,
    'Lime': 0.75,
    'Lemon': 0.80,
    'Sugar': 1.50,
    'Drink sleeve': 0.10,
    'Oolong tea': 2.00,
    'Taro': 1.80,
    'Tea': 1.50,
    'Lid': 0.05,
    'Tapioca pearls': 2.50,
    'Strawberry': 2.00,
    'Milk tea': 3.00,
    'Matcha': 4.00,
    'Honey': 3.20,
    'Lychee jelly': 2.50,
    'Wintermelon': 1.90,
    'Peach tea': 2.75,
    'Peach': 1.50,
    'Ice': 0.20,
    'Napkin': 0.05,
    'Grapefruit': 1.75,
    'Passion fruit': 2.25,
    'Ginger': 1.00,
    'Orange': 1.25,
    'Straw': 0.05,
    'Black tea': 1.80,
    'Cup': 0.25,
    'Cocoa': 2.75,
    'Kiwi': 1.60,
    'Water': 0.50,
    'Coffee': 2.50,
    'Oreo': 1.20,
    'Okinawa brown sugar': 3.75,
    'Milk': 2.00,
    'Thai tea': 2.50,
    'Papaya': 1.80,
    'Green tea': 2.00,
    'Mango': 2.25,
    'Herb jelly': 2.00,
    'Pineapple': 1.75,
    'Mint': 1.50
}



f = open("names.csv")

NAMES = {}

for i in range(518):
    NAMES[i] = f.readline()

f.close()