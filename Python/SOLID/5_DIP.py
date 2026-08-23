# Without DIP

class PetrolEngine:
    def start(self):
        print("Petrol engine started")


class Car:
    def __init__(self):
        self.engine = PetrolEngine()

    def start(self):
        self.engine.start()


print("-------------------- Without DIP --------------------")

car = Car()
car.start()


# With DIP

class Engine:
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine started")


class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


print("-------------------- With DIP --------------------")

petrol_engine = PetrolEngine()
car = Car(petrol_engine)
car.start()

electric_engine = ElectricEngine()
car = Car(electric_engine)
car.start()