#  Create a class named ‘Dog’. It should have a constructor which accepts its name,
#  age and coat color. You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
    def fetch(self):
        print("Jack Russell Terrier is fetching...")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def eat(self):
        print("Bulldog is eating...")

jack = JackRussellTerrier("Jack", 3, "White")
print(jack.description())
print(jack.get_info())

jack.fetch()

bulldog = Bulldog("Bulldog", 2, "Black")
print(bulldog.description())
print(bulldog.get_info())
bulldog.eat()