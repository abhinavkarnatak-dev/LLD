# Without LSP

class Bird:
    def fly(self):
        print("Bird is flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


print("-------------------- Without LSP --------------------")

sparrow = Sparrow()
sparrow.fly()

penguin = Penguin()
penguin.fly()


# With LSP

class Bird:
    def eat(self):
        print("Bird is eating")


class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")


class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def eat(self):
        print("Penguin is eating")


print("-------------------- With LSP --------------------")

sparrow = Sparrow()
sparrow.fly()

penguin = Penguin()
penguin.eat()