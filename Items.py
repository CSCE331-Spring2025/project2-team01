import constants, random, uuid, math

from Topping import Topping

class Items:
    def __init__(self, Uuid, Flavor, BasePrice, SubFlavor):
        self.Uuid = str(Uuid)
        self.flavor = Flavor
        self.basePrice = BasePrice
        self.subFlavor = SubFlavor
        self.toppings = []


    def getUuid(self):
        return self.Uuid
    
    def getFlavor(self):
        return self.flavor
    
    def getBasePrice(self):
        return self.basePrice

    def getSubFlavor(self):
        return self.subFlavor
    
    def getToppings(self):
        return self.toppings
    
    def getTotalPrice(self):
        sum = self.basePrice
        for t in self.toppings:
            sum += t.getBasePrice()
        return sum
    
    def generateToppings(self, orderItemId, itemId):
        # write a program that picks random toppings from constants
        # pick two random numbers, first is the number of toppings, second is the actual toppings

        # picks a number [1,12] with a median of 3
        numToppings = math.ceil(random.triangular(1, 12, 3))
        # picks numToppings toppings from TOPPINGS randomly
        selectedToppings = random.sample(constants.TOPPINGS, numToppings)
                
        # create Topping objects for each selected topping
        self.toppings = [
            Topping(
                uuid=constants.TOPPINGS.index(topping), 
                type=topping, 
                basePrice=constants.TOPPINGPRICES.get(topping))
            for topping in selectedToppings
        ]
        orderItemToppingsDict = {}
        for topping in self.toppings:
            orderItemToppingsDict[uuid.uuid4()] = {
                            "OrderItemId": orderItemId,
                            "ItemId": itemId,
                            "toppingId": topping.getUuid(),
                            "intensity": max(round(random.gauss(10, 5)), 1) # 10 for 100%, 5 for 50%, 20 for 200%...
            }
        return orderItemToppingsDict
        
    
    def to_dict(self):
        """Convert the Item object to a dictionary for CSV writing."""
        return {
            "Item UUID": str(self.Uuid),
            "Flavor": self.flavor,
            "Base Price": self.basePrice,
            "Sub Flavor": self.subFlavor,
            "Toppings": ", ".join([t.type for t in self.toppings]), 
            "Total Price": self.getTotalPrice()
        }    

    def __repr__(self):
        return f"Items(uuid={self.uuid}, flavor={self.flavor}, basePrice={self.basePrice}, subFlavor={self.subFlavor}, toppings={[t.type for t in self.toppings]})"

