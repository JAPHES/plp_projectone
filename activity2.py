class Vehicle:
    def move(self):
        # Generic move - to be overridden by subclasses
        print("This vehicle is moving in some way.")

class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying through the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚢 Boat is sailing on the water.")

# Create a list of vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Loop through and call move() on each one
for vehicle in vehicles:
    vehicle.move()
