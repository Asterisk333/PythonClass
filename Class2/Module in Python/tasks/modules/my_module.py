class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        print(f"name: {self.name}, Alter: {self.age}, Stadt: {self.city} ")


if __name__ == "__main__":
    person = Person("John", 30, "New York")
    person.info()
