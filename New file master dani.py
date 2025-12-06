class Smartphone:
    # 1. The Setup (__init__)
    # This runs when we make a new phone.
    def __init__(self, brand_name):
        self.brand = brand_name      # Set the brand provided by the user
        self.battery_level = 100     # Set a default value (always starts full)

    # 2. The Action (Method)
    # Notice 'self' is the first parameter! It lets the method find the specific phone's battery.
    def use_app(self, app_name, battery_cost):
        self.battery_level = self.battery_level - battery_cost
        print(f"Opened {app_name}. Battery is now at {self.battery_level}%")

# 3. Creating an Object (Instance)
my_phone = Smartphone("Samsung")

# 4. Using the Object
print(f"My phone is a {my_phone.brand}") # Output: My phone is a Samsung
my_phone.use_app("Instagram", 15)        # Output: Opened Instagram. Battery is now at 85%