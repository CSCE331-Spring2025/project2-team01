import Items
import random
import constants
import uuid

class Orders:
    def __init__(self, Uuid, isFulfilled, dateTime, totalPrice, customerName, employeeId):
        self.Uuid = Uuid
        self.isFulfilled = True
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
        return self.customerName
    def getEmployeeId(self):
        return self.employeeId
    
    def generateItems(self):
        itemsDict = {}
        for i in range(random.randint(1,10)):
            randomFlavor = random.randint(0,5)
            seedState = random.getstate()
            randomSubflavor = random.randint(0,len(constants.MENU[constants.FLAVORS[randomFlavor]])-1)
            random.setstate(seedState)
            randomItem = Items.Items(
                        Uuid=str(uuid.uuid4()),
                        Flavor=constants.FLAVORS[randomFlavor], 
                        BasePrice=constants.FLAVORPRICES[constants.FLAVORS[randomFlavor]], 
                        SubFlavor=constants.MENU[constants.FLAVORS[randomFlavor]][randomSubflavor]
                        )
            randomItem.generateToppings()
            itemsDict[randomItem.Uuid] = randomItem.to_dict()
            self.totalPrice += randomItem.getTotalPrice()
        return itemsDict
        
    def to_dict(self):
        return {
            "Order UUID": self.Uuid,
            "Is Fulfilled": self.isFulfilled,
            "Date Time": self.dateTime,
            "Total Price": self.totalPrice,
            "Customer Name": self.customerName,
            "Employee UUID": self.employeeId
        }