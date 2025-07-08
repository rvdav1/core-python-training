# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show(self):
        raise NotImplementedError

class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"
