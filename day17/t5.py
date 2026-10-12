from dataclasses import dataclass

@dataclass
class Product:
    name:str
    price:float
    quantity: int
    def total_price(self):
        return self.price * self.quantity

product = Product("Laptop", 75000, 2)

print(product.total_price())
