"""Lab Objective: Implement OOP by creating a class and various objects."""


class Car:
    def __init__(self, color, windows_number=5, price = 0):
        self.color = color
        self.windows_number = windows_number
        self.price = price
        
 

car1 = Car("pink",price=10)
car2 = Car("Blue", 2, 300500)

print(vars(car1))
print(vars(car2))
