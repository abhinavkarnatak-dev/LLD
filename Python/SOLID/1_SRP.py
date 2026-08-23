# Without SRP

class Restaurant:
    def take_order(self):
        print("Taking order")

    def cook_food(self):
        print("Cooking food")

    def take_payment(self):
        print("Taking payment")


print("-------------------- Without SRP --------------------")

restaurant = Restaurant()

restaurant.take_order()
restaurant.cook_food()
restaurant.take_payment()


# With SRP

class Waiter:
    def take_order(self):
        print("Taking order")


class Chef:
    def cook_food(self):
        print("Cooking food")


class Cashier:
    def take_payment(self):
        print("Taking payment")


print("-------------------- With SRP --------------------")

waiter = Waiter()
waiter.take_order()

chef = Chef()
chef.cook_food()

cashier = Cashier()
cashier.take_payment()