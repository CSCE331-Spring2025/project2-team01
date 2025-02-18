import constants, random,uuid, math, Topping

class Items:
    def __init__(self, Uuid, Flavor, BasePrice, SubFlavor):
        self.uuid = Uuid
        self.flavor = Flavor
        self.basePrice = BasePrice
        self.subFlavor = SubFlavor
        self.toppings = []

    def getUuid(self):
        return self.uuid
    
    def getFlavor(self):
        return self.flavor
    
    def getBasePrice(self):
        return self.basePrice

    def getSubFlavor(self):
        return self.subFlavor
    
    def getToppings(self):
        return self.toppings
    
    def generateToppings(self):
        # write a program that picks random toppings from constants
        # pick two random numbers, first is the number of toppings, second is the actual toppings

        # picks a number [1,12] with a median of 3
        numToppings = math.ceil(random.triangular(1, 12, 3))
        # picks numToppings toppings from TOPPINGS randomly
        selectedToppings = random.sample(constants.TOPPINGS, numToppings)
                
        # create Topping objects for each selected topping
        self.toppings = [
            Topping(str(uuid.uuid4()), topping, constants.TOPPINGPRICES.get(topping, 0.50)) 
            for topping in selectedToppings
        ]

    def to_dict(self):
        """Convert the Item object to a dictionary for CSV writing."""
        return {
            "Item UUID": self.uuid,
            "Flavor": self.flavor,
            "Base Price": self.basePrice,
            "Sub Flavor": self.subFlavor,
            "Toppings": ", ".join([t.type for t in self.toppings]), 
            "Total Price": self.getTotalPrice()
        }    

    def __repr__(self):
        return f"Items(uuid={self.uuid}, flavor={self.flavor}, basePrice={self.basePrice}, subFlavor={self.subFlavor}, toppings={[t.type for t in self.toppings]})"
