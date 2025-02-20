import Items
import random
import constants
import uuid
import csv
import os

class Orders:
    def __init__(self, Uuid, isFulfilled, dateTime, totalPrice, customerName, employeeId):
        self.Uuid = Uuid  # Generate a unique order ID if not provided
        self.isFulfilled = isFulfilled  # Boolean indicating fulfillment status
        self.dateTime = dateTime  # Default to current time
        self.customerName = customerName  # Random customer
        self.employeeId = employeeId  # Random employee
        self.totalPrice = 0.0  # Initialize total price

    def generateItems(self):
        orderItemsDict = {}
        for i in range(random.randint(1,10)):
            randomFlavor = random.randint(0,5)
            seedState = random.getstate()
            randomSubflavor = random.randint(0,len(constants.MENU[constants.FLAVORS[randomFlavor]])-1)
            random.setstate(seedState)
            randomItem = Items.Items(
                        Uuid=constants.get_item_number(randomFlavor, randomSubflavor),
                        Flavor=constants.FLAVORS[randomFlavor], 
                        BasePrice=constants.FLAVORPRICES[constants.FLAVORS[randomFlavor]], 
                        SubFlavor=constants.MENU[constants.FLAVORS[randomFlavor]][randomSubflavor]
                        )
            orderItemId = uuid.uuid4()
            orderItemToppingsDict = randomItem.generateToppings(orderItemId, randomItem.getUuid())
            orderItemsDict[orderItemId] = {
                            "orderId": self.getUuid(),
                            "itemId": randomItem.getUuid(),
                            "quantity": 1,
                            "subTotal": round(randomItem.getTotalPrice(), 2)
            }
            Orders.write_orderItemToppings_to_csv(orderItemToppingsDict)
                            
            self.totalPrice += randomItem.getTotalPrice()
        return orderItemsDict

    def updateTotalPrice(self):
        """Updates and returns the total price of all drinks in the order."""
        self.totalPrice = sum(drink.getTotalPrice() for drink in self.items)

    def getUuid(self):
        return self.Uuid

    def getIsFulfilled(self):
        return self.isFulfilled

    def getDateTime(self):
        return self.dateTime

    def getTotalPrice(self):
        return self.totalPrice  # Returns the updated total price

    def getCustomerName(self):
        return self.customerName

    def getEmployeeId(self):
        return self.employeeId

    def to_dict(self):
        """Convert the Order object to a dictionary for CSV export."""
        return {
            "OrderUUID": self.Uuid,
            "IsFulfilled": self.isFulfilled,
            "DateTime": self.dateTime,
            "TotalPrice": self.totalPrice,
            "CustomerName": self.customerName,
            "EmployeeUUID": self.employeeId
        }
    
    def write_orderItemToppings_to_csv(orderItemToppingsDict, filename="orderItemToppings.csv"):
        """Writes itemDict to a CSV file, appending if the file exists."""
        if not orderItemToppingsDict:
            print("No data to write.")
            return
        # Extract field names dynamically from the first item
        fieldnames = list(next(iter(orderItemToppingsDict.values())).keys())
        file_exists = os.path.isfile(filename)  # Check if file exists
        with open(filename, mode="a" if file_exists else "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:  
                writer.writeheader()  # Write header only if file is new
            for item in orderItemToppingsDict.values():
                #item["Item UUID"] = str(item["Item UUID"])
                #item["subTotal"] = round(item["subTotal"], 2)  # Round Total Price

                writer.writerow(item)

        #print(f"✅ Data written to '{filename}' successfully.")