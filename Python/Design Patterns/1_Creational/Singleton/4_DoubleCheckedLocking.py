# Ensures lazy loading is thread safe
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:                               # First check if no instance
            with cls._lock:                                     # Then lock
                if cls._instance is None:                       # Then check again and create instance
                    cls._instance = super().__new__(cls)

        return cls._instance

# Same instances
instance1 = Singleton()
instance2 = Singleton()

print(instance1)
print(instance2)
print(instance1 is instance2)