class Topping:
    def __init__(self, uuid:str, type:str, basePrice:float):
        self.uuid = uuid
        self.type = type
        self.basePrice = basePrice

    def getUuid(self)->str:
        return self.uuid
    
    def getType(self)->str:
        return self.type

    def getBasePrice(self)->float:
        return self.basePrice
    
    
