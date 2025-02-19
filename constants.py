import random
import uuid

random.seed(10)

MENU = {
    "Brewed tea": [
        "Classicblack",
        "Classicgreen",
        "Classicoolong",
        "Honeyblack",
        "Honeygreen",
        "Honeyoolong",
        "Ginger",
        "Wintermelon"
    ],
    "Milktea": [
        "Honeymilkblack",
        "Honeymilkgreen",
        "Honeyoolong",
        "Mangogingermilk",
        "Coffeemilk",
        "Thaimilk",
        "Classic",
        "Taro",
        "Okinawamilk",
        "Matchamilk",
        "Hokkaido",
        "Gingermilk",
        "QQhappyfamily",
        "Classiccoffee"
    ],
    "Fruit tea": [
        "Hawaiifruittea",
        "Honeylemonade",
        "Kiwifruittea",
        "Passionfruitorangeandgrapefruit",
        "Strawberry",
        "Tropicalfruit",
        "Mangoandpassionfruit",
        "Peachkiwi",
        "Peach",
        "Wintermelonlemonade",
        "Mangogreen"
    ],
    "Fresh milk": [
        "Freshmilkblacktea",
        "Freshmilkgreentea",
        "Freshmilkoolongtea",
        "Wintermelonwithfreshmilk",
        "Cocoaloverwithfreshmilk",
        "Matchawithfreshmilk",
        "Freshmilkfamily",
        "Handmadetarowithfreshmilk"
    ],
    "Ice blended": [
        "Milkteaiceblended",
        "Peachteaiceblended",
        "Thaiteaiceblended",
        "Taroiceblended",
        "Strawberryiceblended",
        "Oreoiceblended",
        "Coffeeiceblended",
        "Mangoiceblended",
        "Matchaiceblended"
    ],
    "Tea mojito": [
        "Limemojito",
        "Strawberrymojito",
        "Mangomojito",
        "Peachmojito"
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
    "Lycheejelly",
    "Pudding",
    "Aloe vera",
    "Herbjelly",
    "Crema",
    "Aiyu jelly",
    "Ice cream",
    "Honey pack",
    "Edible green"
]

ITEMSINGREDIENTS = {
    "Classicblack": ["Blacktea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Classicgreen": ["Greentea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Classicoolong": ["Oolongtea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeyblack": ["Blacktea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeygreen": ["Greentea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeyoolong": ["Oolongtea", "Honey", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Ginger": ["Ginger", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Wintermelon": ["Wintermelon", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeymilkblack": ["Blacktea", "Honey", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeymilkgreen": ["Greentea", "Honey", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeyoolong": ["Oolongtea", "Honey", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Mangogingermilk": ["Mango", "Ginger", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Coffeemilk": ["Coffee", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Thaimilk": ["Thaitea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Classic": ["Blacktea", "Sugar", "Water", "Milk", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Taro": ["Taro", "Sugar", "Milk", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Okinawamilk": ["Okinawabrownsugar", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Matchamilk": ["Matcha", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Hokkaido": ["Hokkaidomilk", "Sugar", "Water", "Milk", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Gingermilk": ["Ginger", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "QQhappyfamily": ["Tapiocapearls", "Herbjelly", "Lycheejelly", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Classiccoffee": ["Coffee", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Hawaiifruittea": ["Pineapple", "Mango", "Lemon", "Tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Honeylemonade": ["Honey", "Lemon", "Water", "Sugar", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Kiwifruittea": ["Kiwi", "Tea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Passionfruitorangeandgrapefruit": ["Passionfruit", "Orange", "Grapefruit", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Strawberry": ["Strawberry", "Sugar", "Water", "Ice", "Lemon", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Tropicalfruit": ["Mango", "Pineapple", "Papaya", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Mangoandpassionfruit": ["Mango", "Passionfruit", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Peachkiwi": ["Peach", "Kiwi", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Peach": ["Peach", "Sugar", "Water", "Ice", "Lemon", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Wintermelonlemonade": ["Wintermelon", "Lemon", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Mangogreen": ["Mango", "Greentea", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Freshmilkblacktea": ["Blacktea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Freshmilkgreentea": ["Greentea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Freshmilkoolongtea": ["Oolongtea", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Wintermelonwithfreshmilk": ["Wintermelon", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Cocoaloverwithfreshmilk": ["Cocoa", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Matchawithfreshmilk": ["Matcha", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Freshmilkfamily": ["Milk", "Sugar", "Water", "Ice", "Tapiocapearls", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Handmadetarowithfreshmilk": ["Taro", "Milk", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Milkteaiceblended": ["Milktea", "Ice", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Peachteaiceblended": ["Peachtea", "Ice", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Thaiteaiceblended": ["Thaitea", "Ice", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Taroiceblended": ["Taro", "Ice", "Sugar", "Water", "Milk", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Strawberryiceblended": ["Strawberry", "Ice", "Sugar", "Water", "Milk", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Oreoiceblended": ["Oreo", "Ice", "Milk", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Coffeeiceblended": ["Coffee", "Ice", "Milk", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Mangoiceblended": ["Mango", "Ice", "Sugar", "Water", "Milk", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Matchaiceblended": ["Matcha", "Ice", "Milk", "Sugar", "Water", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Limemojito": ["Lime", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Strawberrymojito": ["Strawberry", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Mangomojito": ["Mango", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"],
    "Peachmojito": ["Peach", "Mint", "Sugar", "Water", "Ice", "Cup", "Straw", "Lid", "Napkin", "Drinksleeve"]
}

FLAVORPRICES = {
    "Brewed tea": 4.25,
    "Milktea": 4.75,
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
    "Lycheejelly": 0.75,
    "Pudding": 0.70,
    "Aloe vera": 0.65,
    "Herbjelly": 0.55,
    "Crema": 0.80,
    "Aiyu jelly": 0.70,
    "Ice cream": 1.50,
    "Honey pack": 0.40,
    "Edible green": 0.60
}

FLAVORS = [
    "Brewed tea",
    "Milktea",
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

EMPLOYEEUUIDS = [
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            str(uuid.uuid4())
]

ALLERGENS = {
    'Hokkaidomilk': True,
    'Lime': False,
    'Lemon': False,
    'Sugar': False,
    'Drinksleeve': False,
    'Oolongtea': False,
    'Taro': False,
    'Tea': False,
    'Lid': False,
    'Tapiocapearls': False,
    'Strawberry': False,
    'Milktea': True,
    'Matcha': False,
    'Honey': False,
    'Lycheejelly': False,
    'Wintermelon': False,
    'Peachtea': False,
    'Peach': False,
    'Ice': False,
    'Napkin': False,
    'Grapefruit': False,
    'Passionfruit': False,
    'Ginger': False,
    'Orange': False,
    'Straw': False,
    'Blacktea': False,
    'Cup': False,
    'Cocoa': True,
    'Kiwi': True,
    'Water': False,
    'Coffee': False,
    'Oreo': True,
    'Okinawabrownsugar': False,
    'Milk': True,
    'Thaitea': True,
    'Papaya': False,
    'Greentea': False,
    'Mango': False,
    'Herbjelly': False,
    'Pineapple': False,
    'Mint': False,
    "Pearl": False,
    "Crystal boba": False,
    "Mini pearl": False,
    "Lycheejelly": False,
    "Pudding": True,  # May contain dairy or eggs
    "Aloe vera": False,
    "Herbjelly": False,
    "Crema": True,  # Often contains dairy
    "Aiyu jelly": False,
    "Ice cream": True,  # Contains dairy
    "Honey pack": False,
    "Edible green": False
}

MATERIALUNITPRICE = {
    "Pearl": 0.50,
    "Crystal boba": 0.60,
    "Mini pearl": 0.55,
    "Lycheejelly": 0.70,
    "Pudding": 0.75,
    "Aloe vera": 0.80,
    "Herbjelly": 0.65,
    "Crema": 0.90,
    "Aiyu jelly": 0.85,
    'Ice cream': 1.00,
    "Honey pack": 0.95,
    "Edible green": 0.60,
    'Hokkaidomilk': 3.50,
    'Lime': 0.75,
    'Lemon': 0.80,
    'Sugar': 1.50,
    'Drinksleeve': 0.10,
    'Oolongtea': 2.00,
    'Taro': 1.80,
    'Tea': 1.50,
    'Lid': 0.05,
    'Tapiocapearls': 2.50,
    'Strawberry': 2.00,
    'Milktea': 3.00,
    'Matcha': 4.00,
    'Honey': 3.20,
    'Lycheejelly': 2.50,
    'Wintermelon': 1.90,
    'Peachtea': 2.75,
    'Peach': 1.50,
    'Ice': 0.20,
    'Napkin': 0.05,
    'Grapefruit': 1.75,
    'Passionfruit': 2.25,
    'Ginger': 1.00,
    'Orange': 1.25,
    'Straw': 0.05,
    'Blacktea': 1.80,
    'Cup': 0.25,
    'Cocoa': 2.75,
    'Kiwi': 1.60,
    'Water': 0.50,
    'Coffee': 2.50,
    'Oreo': 1.20,
    'Okinawabrownsugar': 3.75,
    'Milk': 2.00,
    'Thaitea': 2.50,
    'Papaya': 1.80,
    'Greentea': 2.00,
    'Mango': 2.25,
    'Herbjelly': 2.00,
    'Pineapple': 1.75,
    'Mint': 1.50
}


NAMES = [
    "Owen Henderson",
    "Eric Kelly",
    "Alexia Ross",
    "Ellia Edwards",
    "Victoria Stewart",
    "Lilianna Richardson",
    "Joyce Taylor",
    "Emily Armstrong",
    "Brianna Carter",
    "Thomas Evans",
    "Jared Elliott",
    "Amber Montgomery",
    "Tony Taylor",
    "Honey Harris",
    "Aldus Roberts",
    "Richard Hunt",
    "Eleanor Wright",
    "Mary Baker",
    "Tara Payne",
    "Henry Roberts",
    "Jasmine Richardson",
    "Leonardo Harrison",
    "Tara Elliott",
    "Roland Brown",
    "Fiona Wells",
    "Martin Johnston",
    "Abraham Hunt",
    "James Barnes",
    "Clark Alexander",
    "Adrianna Holmes",
    "Preston Perkins",
    "Tess Taylor",
    "Preston Mitchell",
    "Caroline Cole",
    "Adelaide Gibson",
    "Miranda Armstrong",
    "Catherine Roberts",
    "Lana Bailey",
    "Preston Bennett",
    "Alford Fowler",
    "Maria Elliott",
    "Miley Dixon",
    "Adrian Mitchell",
    "Dale Gray",
    "Cherry Harris",
    "Jack Douglas",
    "Evelyn Ryan",
    "Lyndon Phillips",
    "Roman Riley",
    "Jessica Moore",
    "Justin Andrews",
    "Carlos Baker",
    "Robert Bailey",
    "Carlos Craig",
    "Daisy Hamilton",
    "Heather Craig",
    "Nicole Craig",
    "Nicole Richards",
    "James Nelson",
    "Adison Thomas",
    "Cherry Foster",
    "Olivia Reed",
    "Aldus Cooper",
    "Audrey Casey",
    "Tiana Edwards",
    "Charlie Perkins",
    "Kelvin Wells",
    "Carina Henderson",
    "Anna Carter",
    "Nicole Phillips",
    "Jessica Riley",
    "Tess Mason",
    "Caroline Ross",
    "Jessica Perry",
    "Amber Hall",
    "Victor Walker",
    "Adrianna Carter",
    "Brianna Payne",
    "Briony Carroll",
    "Olivia Cole",
    "Stuart Howard",
    "Blake Clark",
    "Adrianna Hamilton",
    "Sydney Allen",
    "Chelsea Richards",
    "Lenny Barnes",
    "Emily Perkins",
    "Haris Mason",
    "Kate Higgins",
    "Jack Hamilton",
    "Kirsten Mason",
    "Henry Thompson",
    "Agata Andrews",
    "Rubie Craig",
    "Maya Cooper",
    "Alfred Holmes",
    "Myra Farrell",
    "Agata Stewart",
    "Brooke Moore",
    "Alisa Henderson",
    "Cherry Morrison",
    "Carlos Cameron",
    "Clark Higgins",
    "Fiona Hall",
    "Lyndon Cunningham",
    "Olivia Douglas",
    "Melissa Dixon",
    "George Hamilton",
    "Alexander Clark",
    "Lilianna Mitchell",
    "Sabrina Brown",
    "Eddy Bennett",
    "Dexter Wright",
    "Derek Brown",
    "Ted Henderson",
    "Carina Taylor",
    "Bruce Dixon",
    "Alan Richardson",
    "Arthur Hill",
    "Aiden Richards",
    "Sofia Cunningham",
    "Eric Alexander",
    "Ashton Nelson",
    "Tess Clark",
    "Elian Harper",
    "Luke Watson",
    "Naomi Stewart",
    "Luke Holmes",
    "Dale Sullivan",
    "Lilianna Turner",
    "Amanda Stevens",
    "Alexander Ferguson",
    "Cadie Morrison",
    "Abigail Turner",
    "Amelia Murphy",
    "Garry Cole",
    "Connie Gray",
    "Amber Richardson",
    "Spike Martin",
    "Eddy Barrett",
    "Naomi Myers",
    "Madaline Cameron",
    "Annabella Wright",
    "Alford Nelson",
    "Henry Morrison",
    "Roland Andrews",
    "Kelvin Morgan",
    "Henry Cameron",
    "Amelia Mitchell",
    "Cherry Kelley",
    "Thomas Holmes",
    "Owen Moore",
    "Edith Armstrong",
    "Byron Kelley",
    "Alan Jones",
    "Edith Stewart",
    "Grace Ferguson",
    "Dominik Harper",
    "Oliver Ferguson",
    "Freddie Alexander",
    "Daryl Andrews",
    "Grace Payne",
    "Sarah Harper",
    "Lucia Owens",
    "Belinda Fowler",
    "Amber Lloyd",
    "Eric Scott",
    "Maddie Harris",
    "Heather Cunningham",
    "Fiona Kelly",
    "Victoria Rogers",
    "Amanda Morris",
    "James Campbell",
    "Alexander Campbell",
    "Richard Williams",
    "Brianna Roberts",
    "Sydney Hill",
    "Amelia Gray",
    "Carl Turner",
    "Edgar Spencer",
    "Derek Ryan",
    "Arthur Reed",
    "Sarah Chapman",
    "Audrey Holmes",
    "Jenna Russell",
    "Kellan Hamilton",
    "Tony Martin",
    "Ryan Watson",
    "Charlie Gibson",
    "April Mason",
    "Mike Ryan",
    "Rosie West",
    "Maximilian Carter",
    "Owen Foster",
    "Lydia Cooper",
    "Eric Davis",
    "Samantha Murray",
    "Deanna Watson",
    "Agata Thomas",
    "Joyce Bailey",
    "Edgar Davis",
    "Alisa Ferguson",
    "Edwin Lloyd",
    "Darcy Higgins",
    "Andrew Jones",
    "Alford West",
    "Chloe Anderson",
    "Ryan Johnson",
    "Sofia Morris",
    "Sofia Hamilton",
    "Vivian Taylor",
    "Frederick Farrell",
    "Aiden Phillips",
    "Miley Reed",
    "Naomi Andrews",
    "Oliver Richards",
    "Adelaide Mason",
    "Nicole Stevens",
    "Lucia Phillips",
    "Dale Warren",
    "Garry West",
    "Alen Payne",
    "Brooke Wright",
    "Melanie Bennett",
    "Maya West",
    "Aldus West",
    "Miley Morgan",
    "Stuart Hamilton",
    "David Taylor",
    "Emma Clark",
    "Rubie Chapman",
    "Jacob Mason",
    "Bruce Williams",
    "Alisa Martin",
    "Mary Morgan",
    "Brad Allen",
    "Valeria West",
    "Lenny Montgomery",
    "Edward Douglas",
    "Gianna Holmes",
    "Audrey Roberts",
    "Ted Martin",
    "Carlos Richardson",
    "Tony Stewart",
    "Charlie Payne",
    "Leonardo Kelley",
    "Miranda Johnston",
    "Ned Rogers",
    "George Howard",
    "Paige Morris",
    "Daryl Craig",
    "Miranda Thompson",
    "Edgar Smith",
    "Harold Armstrong",
    "Victor Montgomery",
    "Lucas West",
    "Henry Ellis",
    "Preston Rogers",
    "Heather Hill",
    "Frederick Crawford",
    "Robert Wilson",
    "Heather Thomas",
    "Alisa Tucker",
    "Lenny Riley",
    "Madaline Howard",
    "Edward Richards",
    "Alen Hill",
    "William Owens",
    "Ashton Douglas",
    "Myra Wells",
    "James Wilson",
    "Daryl Fowler",
    "Jasmine Martin",
    "Owen Cameron",
    "Rafael Warren",
    "Daryl Bennett",
    "Richard Campbell",
    "Evelyn Brown",
    "Heather Hawkins",
    "Alford Thompson",
    "Carlos Smith",
    "Catherine Cole",
    "Victor Myers",
    "Kellan Henderson",
    "Melanie Riley",
    "Dainton Fowler",
    "Mary Riley",
    "Tony Miller",
    "David Roberts",
    "Valeria Cameron",
    "Miley Barnes",
    "Miranda Crawford",
    "Michael Barrett",
    "Florrie Chapman",
    "Adrianna Clark",
    "William Barnes",
    "Catherine Miller",
    "Arthur Craig",
    "Steven Harrison",
    "Jared Wright",
    "Stuart Kelly",
    "Paul Campbell",
    "Eddy Russell",
    "Amelia Henderson",
    "Catherine Ellis",
    "Jordan Perkins",
    "Michael Cameron",
    "John Wells",
    "Naomi Allen",
    "Arnold Cameron",
    "Tess Harper",
    "Lucia Adams",
    "Alexia Baker",
    "Sarah Morgan",
    "Martin Walker",
    "Penelope Ryan",
    "Eddy Barnes",
    "Honey Baker",
    "Aiden Mason",
    "Dominik Owens",
    "Brad Harrison",
    "Rafael Edwards",
    "Anna Chapman",
    "Naomi Morris",
    "Stuart Stevens",
    "Roman Gray",
    "Belinda Gibson",
    "Aldus Hamilton",
    "Carl Thompson",
    "Richard Miller",
    "Elise Harper",
    "Emily Roberts",
    "Maximilian Farrell",
    "Antony Barnes",
    "Adison Elliott",
    "Emma Ross",
    "Daryl Walker",
    "Sydney West",
    "Charlotte Barrett",
    "Elian Grant",
    "Emma Allen",
    "Paige Parker",
    "Tara Harper",
    "David Jones",
    "Oscar Morgan",
    "Jacob Mitchell",
    "Adam Wells",
    "Max Campbell",
    "Arianna Nelson",
    "Lucy Johnson",
    "Martin Grant",
    "Dale Stewart",
    "Amelia Hawkins",
    "Blake Reed",
    "Daisy Andrews",
    "Melanie Wright",
    "Florrie Roberts",
    "Preston Smith",
    "Daniel Gray",
    "George Barrett",
    "Edwin Holmes",
    "Sydney Anderson",
    "Maya Stewart",
    "Charlotte Harris",
    "Catherine Harris",
    "Briony Cunningham",
    "Elian Richards",
    "Frederick Bennett",
    "Sarah Carroll",
    "Byron Ferguson",
    "Lucas Perry",
    "Michael Hawkins",
    "Dainton Anderson",
    "Martin Phillips",
    "Carina Dixon",
    "Clark Ryan",
    "Lenny Crawford",
    "Arianna Cole",
    "Wilson Gray",
    "Nicholas Barnes",
    "Kelsey Turner",
    "Ned Thomas",
    "Sarah Thomas",
    "Deanna Riley",
    "Adrianna Hill",
    "Cadie Russell",
    "Savana Barnes",
    "Henry Andrews",
    "Amber Hamilton",
    "Sienna Martin",
    "Jenna Johnson",
    "Brianna Kelley",
    "Ada Perkins",
    "Blake Harris",
    "Alissa Robinson",
    "Bruce Moore",
    "Arnold Thompson",
    "Arianna Parker",
    "Amelia Higgins",
    "Preston Tucker",
    "Alissa Harrison",
    "Steven Walker",
    "Sawyer Payne",
    "Owen Carroll",
    "Sienna Edwards",
    "Oscar Brown",
    "Sydney Edwards",
    "Abraham Warren",
    "Alexander Barnes",
    "Dexter Myers",
    "Naomi Bailey",
    "Alberta Moore",
    "Jared Grant",
    "Kirsten Davis",
    "Mary Lloyd",
    "Eric Adams",
    "Catherine Thomas",
    "Kimberly Thompson",
    "Fenton Cunningham",
    "Elian Robinson",
    "John Morrison",
    "Ada Kelley",
    "Kevin Kelley",
    "Maddie Riley",
    "Kristian Owens",
    "Ada Rogers",
    "Anna Bennett",
    "Samantha Rogers",
    "Thomas Cunningham",
    "Stella Brown",
    "Sydney Walker",
    "Vanessa Anderson",
    "Madaline Sullivan",
    "Ted Owens",
    "Edgar Chapman",
    "Lana Campbell",
    "Rubie Casey",
    "Fenton Wells",
    "Abraham Ellis",
    "Olivia Warren",
    "Emma Henderson",
    "Amanda Barnes",
    "Wilson Higgins",
    "Stella Evans",
    "Derek Sullivan",
    "Kellan Parker",
    "Gianna Johnson",
    "Abraham Barrett",
    "Aldus Thomas",
    "Grace Perkins",
    "Sam Mitchell",
    "Heather Barrett",
    "Haris Alexander",
    "Lucia Cooper",
    "Victoria Morrison",
    "Alfred Phillips",
    "Ned Morris",
    "George Davis",
    "Abigail Spencer",
    "Byron Richardson",
    "Alfred Clark",
    "Andrew Moore",
    "Dominik Allen",
    "David West",
    "Roland Roberts",
    "Haris Brown",
    "Harold Nelson",
    "Gianna Montgomery",
    "Oliver Hill",
    "Lucas Ryan",
    "Tyler Phillips",
    "Tiana Clark",
    "Oscar Cameron",
    "Eleanor Douglas",
    "Dale Russell",
    "Nicole Warren",
    "Rubie Thomas",
    "Frederick Cooper",
    "Sydney Barnes",
    "Miley Robinson",
    "Cadie Watson",
    "Vincent Howard",
    "Maddie Wells",
    "Paige Thomas",
    "Adrian Hill",
    "Ryan Johnston",
    "Florrie Hall",
    "Daniel Perkins",
    "Grace Riley",
    "George Roberts",
    "Patrick Foster",
    "Abraham Spencer",
    "Charlotte Edwards",
    "Julia Montgomery",
    "Valeria Harrison",
    "Dainton Williams",
    "Emily Owens",
    "Belinda Gray",
    "Rafael Craig",
    "Victor West",
    "Julia Warren",
    "Abigail Chapman",
    "Annabella Watson",
    "Blake Henderson",
    "Valeria Higgins",
    "Kelvin Hawkins",
    "Walter Rogers",
    "Freddie Roberts",
    "Aldus Taylor",
    "Mike Cole",
    "Emma Crawford",
    "Alisa Clark",
    "Ryan Richardson",
    "Noah Garcia",
    "Ausmit Mondal",
    "Siddesh Selvam",
    "Giovan Ramirez Rodarte",
    "Zachary Bauman"
]