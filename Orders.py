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