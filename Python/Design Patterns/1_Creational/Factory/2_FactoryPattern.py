from abc import ABC, abstractmethod


# Product
class Logistics(ABC):

    @abstractmethod
    def send(self):
        pass


# Concrete Products
class Air(Logistics):

    def send(self):
        print("Send by Air")


class Road(Logistics):

    def send(self):
        print("Send by Road")


# Creator
class LogisticsService(ABC):

    @abstractmethod
    def create_logistics(self):
        pass

    def deliver(self):
        logistics = self.create_logistics()
        logistics.send()


# Concrete Creators
class AirLogisticsService(LogisticsService):

    def create_logistics(self):
        return Air()


class RoadLogisticsService(LogisticsService):

    def create_logistics(self):
        return Road()


# Client
client_choice = AirLogisticsService()
client_choice.deliver()