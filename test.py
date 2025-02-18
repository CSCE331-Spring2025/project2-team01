import uuid
import random
import datetime
import csv
import constants  # Ensure constants.py is correctly imported
import Orders  # Import Orders class

def generate_random_orders(num_orders=10):
    """Generates a dictionary of orders with randomly assigned values."""
    orders_dict = {}

    for _ in range(num_orders):
        order = Orders.Orders(
            Uuid=str(uuid.uuid4()),  # Generate unique order UUID
            isFulfilled=random.choice([True, False]),  # Randomly mark as fulfilled or not
            dateTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Current timestamp
            totalPrice=0,                                #begin price at 0 and add at end
            customerName=random.choice(list(constants.NAMES)),  # Pick random customer name
            employeeId=random.choice(constants.EMPLOYEES)  # Pick random employee ID
        )

        order.generateItems()  # Generate random drinks for order
        orders_dict[order.Uuid] = order.to_dict()  # Convert order to dictionary

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

        for order in orders_dict.values():
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
    orders = generate_random_orders(1000)  # Generate 100 random orders
    write_orders_to_csv(orders)  # Save orders to CSV

    print("\n✅ All tests completed successfully!")

# Run tests
if __name__ == "__main__":
    run_tests()
