class Employee:
    language = "Py"    # This is a class attribute
    salary = 1200000




harry = Employee()
harry.name = "Harry"    # This is an instance attribute
print(harry.name, harry.salary, harry.language)


Rohan = Employee()
Rohan.name = "Rohan"
print(Rohan.name, Rohan.salary, Rohan.language)


# Here name is instance attribute and salary and language are class attributes as they directly belongs to the class
