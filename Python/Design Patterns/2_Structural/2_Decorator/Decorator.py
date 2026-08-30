from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# Concrete component
class PlainPizza(Pizza):
    def get_description(self):
        return "Plain Pizza"

    def get_cost(self):
        return 150
    
class MargheritaPizza(Pizza):
    def get_description(self):
        return "Margherita Pizza"

    def get_cost(self):
        return 200

# Abstract Decorator
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

class ExtraCheese(PizzaDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Extra Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 40

class Olives(PizzaDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    def get_cost(self):
        return self.pizza.get_cost() + 30.0

class StuffedCrust(PizzaDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Stuffed Crust"

    def get_cost(self):
        return self.pizza.get_cost() + 50.0

# Start with a basic Margherita Pizza
my_pizza = MargheritaPizza()

# Add Extra Cheese by wrapping the existing pizza
my_pizza = ExtraCheese(my_pizza)

# Add Olives by wrapping again
my_pizza = Olives(my_pizza)

# Add Stuffed Crust by wrapping again
my_pizza = StuffedCrust(my_pizza)

# Final Description and Cost
print(f"Pizza Description: {my_pizza.get_description()}")
print(f"Total Cost: ₹{my_pizza.get_cost()}")