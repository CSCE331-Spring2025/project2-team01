import uuid
import random
import csv
import constants 

class Employees:
    def __init__(self, Uuid, isManager, name, payGrade, hours):
        self.Uuid = Uuid 
        self.isManager = isManager  
        self.name = name  
        self.payGrade = payGrade  
        self.hours = hours 

    def getUuid(self):
        return self.Uuid

    def getIsManager(self):
        return self.isManager

    def getName(self):
        return self.name

    def getPayGrade(self):
        return self.payGrade

    def getHours(self):
        return self.hours

    def to_dict(self):
        """Convert the Employee object to a dictionary for CSV writing."""
        return {
            "Employee UUID": self.Uuid,
            "Is Manager": self.isManager,
            "Name": self.name,
            "Pay Grade": self.payGrade,
            "Hours": self.hours
        }

    def __repr__(self):
        return f"Employees(Uuid={self.Uuid}, isManager={self.isManager}, name={self.name}, payGrade={self.payGrade}, hours={self.hours})"


    def generate_employee_list():
        """Generate a list of employees using constants.py data."""
        employees = []
        
        # Adds the Manager from constants.py
        employees.append(Employees(
            str(uuid.uuid4()), # Creates a unique UUID for the manager
            True, # Sets the bool to True for the manager
            constants.MANAGER, # Gets the manager name from constants.py (Queen Rev)
            round(random.uniform(22.00, 28.00), 2), # Random pay grade between 22.00 and 28.00 for the manager
            8 # Im guessing the manager works 8 hours a day so its a set value
        ))
        
        # To add the rest of the employees
        for employee_name in constants.EMPLOYEES:
            employees.append(Employees(
            str(uuid.uuid4()),  # Creates a unique UUID for the employee
            False,  # Sets the bool to False for the employee
            employee_name, # Gets the employee name from constants.py
            round(random.uniform(13.00, 21.00), 2),  # Random pay grade
            random.randint(3, 8)  # Random work hours
        ))
        
        return employees


    def write_employees_to_csv(filename="employees.csv"):
        """Writes generated employees to a CSV file."""
        employees = Employees.generate_employee_list()
        
        with open(filename, mode="w", newline="") as file:
            fieldnames = ["Employee UUID", "Is Manager", "Name", "Pay Grade", "Hours"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for employee in employees:
                writer.writerow(employee.to_dict())
        
        print(f"CSV file '{filename}' has been created successfully.")


    if __name__ == "__main__":
        write_employees_to_csv()
