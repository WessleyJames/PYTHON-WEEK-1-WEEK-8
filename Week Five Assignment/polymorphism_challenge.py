# polymorphism_challenge.py
# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(f"{v.__class__.__name__}: {v.move()}")
