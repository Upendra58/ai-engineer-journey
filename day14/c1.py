class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def update_year(self, new_year):
        self.year = new_year

    def change_model(self, new_model):
        self.model = new_model
    
    def display_info(self):
        print(f"{self.brand} {self.model} - {self.year}")

car1 = Car("Toyota","Camry", 2024)
car2 = Car("Honda", "Civic", 2023)
car1.display_info()
car2.display_info()
car1.update_year(2025)
car1.display_info()
car1.change_model("Corolla")
car1.display_info()