class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

class Dog(Animal):
    def Bark(self):
        print(" Woof! Woof!") 

class Cat(Animal):
    def Purr(self):
        print(" Meow...")

class DecideAnimalType:
    def __init__(self, type):
        if type == "dog":
            print("\nEnter details of the dog ")
            animal_name = str(input(" => Name of Dog : "))
            animal_colour = str(input(" => Colour of Dog : "))
            name = Dog(animal_name, animal_colour)
            print("\n Let\'s hear what the Doggy says... ")
            name.Bark()

        if type == "cat":
            print("\nEnter details of the cat ")
            animal_name = str(input(" => Name of Cat : "))
            animal_colour = str(input(" => Colour of Cat : "))
            name = Cat(animal_name, animal_colour)
            print("\n Let\'s hear what the Cat says... ")
            name.Purr()

        input("\n[Press ENTER or RETURN to continue]...")

        print("\n" + "-"*37 + "\n")
        print(" * Printing Summary of Program *\n")
        print("- Type of Animal = " + type)
        print("- Name of " + type + " = " + name.name)
        print("- Colour of " + name.name + " = " + name.colour)
        print(" -- Program Finished --")
        print("\n" + "-"*37 + "\n")

def main():
    type = str(input("Enter type of Animal, [Dog] or [Cat] = "))
    type = type.lower()
    if type == "dog" or "cat":
        DecideAnimalType(type)
    else:
        print(" ** Invalid Input, try again! **\n")
        main()

if __name__ == '__main__': 
    print("\n   --------------------------------------------")
    print("   | Demonstration of Classes and Inheritance |")
    print("   --------------------------------------------\n")
    main()
    