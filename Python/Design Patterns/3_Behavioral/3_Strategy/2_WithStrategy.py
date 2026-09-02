from abc import ABC, abstractmethod


# Strategy Interface
class MatchingStrategy(ABC):

    @abstractmethod
    def match(self, rider_location):
        pass


# Concrete Strategy 1
class NearestDriverStrategy(MatchingStrategy):

    def match(self, rider_location):
        print(f"Matching with nearest driver to {rider_location}")


# Concrete Strategy 2
class AirportQueueStrategy(MatchingStrategy):

    def match(self, rider_location):
        print(f"Matching using airport queue for {rider_location}")


# Concrete Strategy 3
class SurgePriorityStrategy(MatchingStrategy):

    def match(self, rider_location):
        print(f"Matching using surge priority near {rider_location}")


# Context
class RideMatchingService:

    def __init__(self, strategy: MatchingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: MatchingStrategy):
        self._strategy = strategy

    def match_rider(self, location):
        self._strategy.match(location)


service = RideMatchingService(AirportQueueStrategy())
service.match_rider("Terminal 1")

service.set_strategy(NearestDriverStrategy())
service.match_rider("Downtown")

service.set_strategy(SurgePriorityStrategy())
service.match_rider("Downtown")