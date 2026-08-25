class Burger:
    def __init__(self, patty, bun):
        # Required
        self.patty = patty
        self.bun = bun

        # Optional
        self.cheese = False
        self.sauce: list = []
        self.drink = "Not selected"
        self.sides = "Not selected"

    def show(self):
        print("Patty:", self.patty)
        print("Bun:", self.bun)
        print("Cheese:", self.cheese)
        print("Sauce:", self.sauce)
        print("Drink:", self.drink)
        print("Sides:", self.sides)


class BurgerBuilder:
    def __init__(self, patty, bun):
        # Required values
        self.burger = Burger(patty, bun)

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_sauce(self, sauce: list):
        self.burger.sauce = sauce
        return self

    def add_drink(self, drink):
        self.burger.drink = drink
        return self

    def add_sides(self, sides):
        self.burger.sides = sides
        return self

    def build(self):
        return self.burger

burger1 = BurgerBuilder("Veg", "Sesame").build()
burger1.show()

print(40*"-")

burger2 = (
    BurgerBuilder("Veg", "Sesame")
    .add_cheese()
    .add_sauce(["Mayo", "Tandoori"])
    .build()
)
burger2.show()

print(40*"-")

burger3 = (
    BurgerBuilder("Chicken", "Brown")
    .add_cheese()
    .add_sauce(["BBQ"])
    .add_drink("Coke")
    .add_sides("Fries")
    .build()
)
burger3.show()