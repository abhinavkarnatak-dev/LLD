# Not thread safe

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

# Here they are same instances, but could be diff if race condition occurs
instance1 = Singleton()
instance2 = Singleton()

print(instance1)
print(instance2)
print(instance1 is instance2)