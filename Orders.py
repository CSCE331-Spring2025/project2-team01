import uuid
import random
import constants  # Ensure this is correctly imported
from Items import Items  # Import Items class

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
            "Order UUID": self.Uuid,
            "Is Fulfilled": self.isFulfilled,
            "Date & Time": self.dateTime,
            "Total Price": round(self.totalPrice, 2),
            "Customer Name": self.customerName,
            "Employee ID": self.employeeId,
            "Items": " | ".join([f"{drink.flavor} ({drink.subFlavor}) - ${drink.getTotalPrice():.2f}" for drink in self.items])  # Drinks summary
        }

    def __repr__(self):
        return f"Orders(Uuid={self.Uuid}, isFulfilled={self.isFulfilled}, dateTime={self.dateTime}, totalPrice={self.totalPrice:.2f}, customerName={self.customerName}, employeeId={self.employeeId}, items={[drink.flavor for drink in self.items]})"
