import constants, random, math
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
    
    def generateToppings(self):
        # write a program that picks random toppings from constants
        # pick two random numbers, first is the number of toppings, second is the actual toppings

        # picks a number [1,12] with a median of 3
        numToppings = math.ceil(random.triangular(1, 12, 3))
        # picks numToppings toppings from TOPPINGS randomly
        self.toppings = random.sample(constants.TOPPINGS, numToppings)
    
    def getToppings(self):
        return self.toppings