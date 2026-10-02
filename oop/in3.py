# method overriding

class Animal: # parent class
    def speak(self): 
        print("Animals bark")
class Dog(Animal): # child class
    def speak(self):
        print("Dog barks bow bow")
class Cat(Animal): # child class inherit parent (Animal)
    def speak(self):
        print("Cat barks mew mew")
animal = Animal()
animal.speak()
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()
