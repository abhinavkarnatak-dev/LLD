class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def display(self, indent):
        print(f"{indent} Product: {self.name} - \u20B9{self.price}")

class ProductBundle():
    def __init__(self, bundle_name):
        self.bundle_name = bundle_name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_price(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def display(self, indent):
        print(f"{indent} Bundle: {self.bundle_name}")
        for product in self.products:
            product.display(indent + " ")

book = Product("Book", 500)
headphones = Product("Headphones", 1500)
charger = Product("Charger", 800)
pen = Product("Pen", 20)
notebook = Product("Notebook", 60)

# Bundle: Iphone Combo
iphone_combo = ProductBundle("iPhone Combo Pack")
iphone_combo.add_product(headphones)
iphone_combo.add_product(charger)

# Bundle: School Kit
school_kit = ProductBundle("School Kit")
school_kit.add_product(pen)
school_kit.add_product(notebook)

# Cart stores mixed types, so client ends up manually branching
cart = [book, iphone_combo, school_kit]

print("Cart Details:\n")

total = 0.0

# Client has to check what it is dealing with
for item in cart:
    if isinstance(item, Product):
        item.display("  ")
        total += item.get_price()
    elif isinstance(item, ProductBundle):
        item.display("  ")
        total += item.get_price()

print(f"\nTotal Price: \u20B9{total}")