# Base class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self._strength_level = strength_level  # Protected attribute (encapsulation)

    def display_info(self):
        print(f"🦸 Superhero: {self.name}")
        print(f"✨ Power: {self.power}")
        print(f"💪 Strength Level: {self._strength_level}")

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    def boost_strength(self, amount):
        self._strength_level += amount
        print(f"{self.name}'s strength increased to {self._strength_level}!")

# Subclass (Inheritance + Polymorphism)
class Villain(Superhero):
    def __init__(self, name, power, strength_level, evil_plan):
        super().__init__(name, power, strength_level)
        self.__evil_plan = evil_plan  # Private attribute (encapsulation)

    # Polymorphism: overriding attack method
    def attack(self):
        print(f"{self.name} strikes with {self.power} and shouts: 'You can't stop me!'")

    def reveal_plan(self):
        print(f"{self.name}'s evil plan is: {self.__evil_plan}")

# Creating objects
hero = Superhero("SolarMan", "Solar Beam", 80)
villain = Villain("DarkMist", "Shadow Smoke", 75, "Block out the sun forever")

# Using methods
hero.display_info()
hero.attack()
hero.boost_strength(10)

print("\n---\n")

villain.display_info()
villain.attack()
villain.reveal_plan()
