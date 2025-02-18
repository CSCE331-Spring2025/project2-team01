import uuid
import random
import datetime
import csv
import constants  # Ensure constants.py is correctly imported
import Orders  # Import Orders class

def generate_random_orders():
    """Generates a dictionary of orders with randomly assigned values."""
    orders_dict = {}
    startDate = datetime.datetime(2016, 5, 28, 9) #start on harambe's death day (dihhs out for harambe)
    currentDate = startDate
    
    
    for i in range(364):
        peakDayFlag = False
        for peakDateString in constants.PEAKDAYS:
            peakDate = datetime.datetime.strptime(peakDateString, "%B %d, %Y")
            if ((peakDate.month == currentDate.month) and (peakDate.day == currentDate.day)):
                peakDayFlag = True

        while(True):
            if(peakDayFlag):
                delta = datetime.timedelta(minutes=random.randint(1,8), seconds=random.randint(1,24))
            else:
                delta = datetime.timedelta(minutes=random.randint(1,23), seconds=random.randint(1,53))
            currentDate += delta
            if(currentDate.hour > 18):
                break
            
            order = Orders.Orders(
                Uuid=str(uuid.uuid4()),  # Generate unique order UUID
                isFulfilled=True,  # Randomly mark as fulfilled or not
                dateTime=currentDate,  # Current timestamp
                totalPrice=0.0,                                #begin price at 0 and add at end
                customerName=random.choice(list(constants.NAMES)),  # Pick random customer name
                employeeId=random.choice(constants.EMPLOYEES)  # Pick random employee ID
            )
            order.generateItems()  # Generate random drinks for order
            orders_dict[order.Uuid] = order.to_dict()  # Convert order to dictionary
        currentDate += datetime.timedelta(days=1)
        currentDate = currentDate.replace(hour=9, minute=0, second=0)

    return orders_dict

def write_orders_to_csv(orders_dict, filename="orders.csv"):
    """Writes orders to a CSV file using DictWriter."""
    with open(filename, mode="w", newline="") as file:
        if not orders_dict:
            print("No data to write.")
            return

        # Extract field names dynamically from first order
        fieldnames = list(next(iter(orders_dict.values())).keys())

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        # Check if 'Total Price' exists and round it
        for order in orders_dict.values():
            if "Total Price" in order and isinstance(order["Total Price"], (int, float)):
                order["Total Price"] = round(order["Total Price"], 2)

            writer.writerow(order)

    print(f"✅ CSV file '{filename}' has been created successfully.")

def run_tests():
    """Runs tests for the Orders class."""
    print("🔹 Running Tests for Orders Class...")

    # Test 1: Create a Single Order and Print
    print("\n🔹 Test 1: Create a Single Order and Print")
    single_order = Orders.Orders(
        Uuid=str(uuid.uuid4()),
        isFulfilled=False,
        dateTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        totalPrice=10.00,
        customerName="Test Customer",
        employeeId="Paul Taele"
    )
    single_order.generateItems()
    print(single_order)

    # Test 2: Generate Multiple Orders and Save to CSV
    print("\n🔹 Test 2: Generate Multiple Orders and Save to CSV")
    orders = generate_random_orders()  # Generate 1000 random orders
    write_orders_to_csv(orders)  # Save orders to CSV

    print("\n✅ All tests completed successfully!")

# Run tests
if __name__ == "__main__":
    run_tests()
