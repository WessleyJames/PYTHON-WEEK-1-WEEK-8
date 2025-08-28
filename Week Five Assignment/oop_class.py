# oop_class.py
# Assignment 1: Design Your Own Class

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)  # Call parent constructor
        self.price = price

    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def phone_info(self):
        return f"Smartphone: {self.device_info()}, Price: ${self.price}"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S22", 999)
    phone2 = Smartphone("Apple", "iPhone 14", 1199)

    print(phone1.phone_info())
    print(phone1.make_call("123-456-7890"))
    print(phone2.phone_info())
    print(phone2.send_message("987-654-3210", "Hello from Python!"))
