# Without ISP

class Ola:
    def book_ride(self):
        print("Ride booked")

    def accept_ride(self):
        print("Ride accepted")

    def start_ride(self):
        print("Ride started")

    def rate_driver(self):
        print("Driver rated")


class Driver(Ola):
    pass


class Rider(Ola):
    pass


print("-------------------- Without ISP --------------------")

driver = Driver()
driver.accept_ride()
driver.start_ride()

rider = Rider()
rider.book_ride()
rider.rate_driver()


# With ISP

class Rider:
    def book_ride(self):
        print("Ride booked")

    def rate_driver(self):
        print("Driver rated")


class Driver:
    def accept_ride(self):
        print("Ride accepted")

    def start_ride(self):
        print("Ride started")


print("-------------------- With ISP --------------------")

rider = Rider()
rider.book_ride()
rider.rate_driver()

driver = Driver()
driver.accept_ride()
driver.start_ride()