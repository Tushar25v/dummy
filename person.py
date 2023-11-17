class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

#the chanjbkjjkn.,nhnugkjnkkklnk
person_instance = Person(name="John Doe", age=30)
employee_instance = Employee(name="Jane Smith", age=25, employee_id="EMP123")


print("Person Information:")
person_instance.display_info()
print("\nEmployee Information:")
employee_instance.display_info()
