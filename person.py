class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __str__(self):
        return f"Person({self.name}, {self.age})"
