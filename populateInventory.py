class Inventory:
    def __init__(self, Uuid, Name, isAllergen, StockQuantity, UnitPrice, Cost):
        self.Uuid = Uuid
        self.Name = Name
        self.isAllergen = isAllergen
        self.StockQuantity = StockQuantity
        self.UnitPrice = UnitPrice
        self.Cost = Cost
    def getUuid(self):
        return self.Uuid
    def getName(self):
        return self.Name
    def getIsAllergen(self):
        return self.isAllergen
    def getStockQuantity(self):
        return self.StockQuantity
    def getUnitPrice(self):
        return self.UnitPrice
    def getCost(self):
        return self.Cost
    
    
    