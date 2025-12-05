class car:

  def __init__(self, brand, color, power):
    self.brand = brand
    self.color = color
    self.power = power

  def start_engine(self):
    print("self pushed engine started")

  def drive(self):
    print("tires rolling")

car1 = car("audi", "black", 1000)
car2 = car("bmw", "white", 2000)

car1.start_engine()
car2.drive()

print(car1.brand)
print(car2.color)
print(car1.power)