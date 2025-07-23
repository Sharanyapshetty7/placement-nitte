class Student:
    def _init_(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Sunshine", "23AI45", 89)
student1.display()
