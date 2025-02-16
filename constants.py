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
    "Honey Green": ["Green tea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drink sleeve"],
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


f = open("names.csv")

NAMES = {}

for i in range(518):
    NAMES[i] = f.readline()

f.close()