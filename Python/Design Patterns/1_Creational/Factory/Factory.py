from abc import ABC, abstractmethod

class Logistics(ABC):
    @abstractmethod
    def send(self):
        pass

class Air(Logistics):
    def send(self):
        print("Send by Air")

class Road(Logistics):
    def send(self):
        print("Send by Road")

class LogisticsFactory:
    def create(self, mode):
        if mode == "Air":
            return Air()
        else:
            return Road()

class LogisticsService:
    def __init__(self, mode):
        self.mode = mode
        self.factory = LogisticsFactory()
    def deliver(self):
        logistics = self.factory.create(self.mode)
        logistics.send()

# Client doesn't wanna know where the 'Air' object is created
client_choice = LogisticsService("Air")
client_choice.deliver()