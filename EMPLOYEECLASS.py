class Employee:
    def _init_(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ₹{self.salary}")

# Example usage
emp1 = Employee("Ananya", 101, 45000)
emp1.display_details()
