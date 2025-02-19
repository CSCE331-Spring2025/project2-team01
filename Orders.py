import Items
import random
import constants
import uuid
import csv
import os

class Orders:
    def __init__(self, Uuid=None, isFulfilled=False, dateTime=None, customerName=None, employeeId=None):
        self.Uuid = Uuid  # Generate a unique order ID if not provided
        self.isFulfilled = isFulfilled  # Boolean indicating fulfillment status
        self.dateTime = dateTime  # Default to current time
        self.customerName = customerName  # Random customer
        self.employeeId = employeeId  # Random employee
        self.items = []  # Store drinks for this order
        self.totalPrice = 0.0  # Initialize total price

    def generateItems(self):
        """Generates a random number of drinks (1-5) for the order and saves them in `self.items`."""
        num_drinks = random.randint(1, 5)  # Choose 1 to 5 drinks per order

        for _ in range(num_drinks):
            # Select a random flavor category
            flavor = random.choice(list(constants.MENU.keys()))
            # Select a sub-flavor from the chosen category
            sub_flavor = random.choice(constants.MENU[flavor])
            # Get base price from FLAVORPRICES
            base_price = constants.FLAVORPRICES.get(flavor, 5.00)  # Default to $5.00 if missing

            # Create an Item (drink)
            drink = Items(str(uuid.uuid4()), flavor, base_price, sub_flavor)
            drink.generateToppings()  # Add random toppings to the drink
            self.items.append(drink)  # Store drink in order

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