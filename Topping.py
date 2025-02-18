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
    
    
    def to_dict(self):
        """Convert the Topping object to a dictionary for CSV writing."""
        return {
            "Topping UUID": self.uuid,
            "Topping Type": self.type,
            "Topping Price": self.basePrice
        }

    def __repr__(self):
        return f"Topping(uuid={self.uuid}, type={self.type}, basePrice={self.basePrice})"
