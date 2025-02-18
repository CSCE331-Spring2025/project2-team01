import math
import Items
import random
import constants
import uuid

class Orders:
    def __init__(self, Uuid, isFulfilled, dateTime, totalPrice, customerName, employeeId):
        self.Uuid = Uuid
        self.isFulfilled = isFulfilled
        self.dateTime = dateTime
        self.totalPrice = totalPrice
        self.customerName = customerName
        self.employeeId = employeeId
    def getUuid(self):
        return self.Uuid
    def getIsFulfilled(self):
        return self.isFulfilled
    def getDateTime(self):
        return self.dateTime
    def getTotalPrice(self):
        return self.totalPrice
    def getCustomerName(self):
        return self.getCustomerName
    def getEmployeeId(self):
        return self.employeeId
    
    def generateItems(self):
        items = []
        for i in range(math.floor(random.random()*10)):
            randomFlavor = math.floor(random.random()*6)
            seedState = random.getstate()
            randomSubflavor = math.floor(random.random()*len(constants.MENU[constants.FLAVORS[randomFlavor]]))
            random.setstate(seedState)
            randomItem = Items.Items(str(uuid.uuid4), constants.FLAVORS[randomFlavor], constants.FLAVORPRICES[constants.FLAVORS[randomFlavor]], constants.MENU[constants.FLAVORS[randomFlavor]][randomSubflavor])
            randomItem.generateToppings
            items.append(randomItem)
            print(randomItem.getTotalPrice())
            self.totalPrice += randomItem.getTotalPrice()
        
    def to_dict(self):
        return {
            "Order UUID": self.Uuid,
            "Is Fulfilled": self.isFulfilled,
            "Date Time": self.dateTime,
            "Total Price": self.totalPrice,
            "Customer Name": self.customerName,
            "Employee UUID": self.employeeId
        }