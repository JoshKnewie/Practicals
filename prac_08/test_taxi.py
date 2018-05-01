from taxi import Taxi

taxi1 = Taxi("Prius 1", 100)
assert taxi1.drive(10)
print(taxi1)
print("Current Fare = ", taxi1.get_fare())
taxi1.start_fare()
taxi1.drive(100)
print(taxi1, "Current fare is", taxi1.get_fare())