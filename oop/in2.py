class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand: {self.brand}")
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) #inheritance from parent class vehicle
        self.model = model
car = Car("Toyota", "Fortuner")
car.show_brand()
print(car.model)
        
