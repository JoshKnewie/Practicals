from prac_08.unreliable_car import UnreliableCar

HyundaiGetz = UnreliableCar("Hyundai Getz", 100, 30)
assert HyundaiGetz.drive(10)
print(HyundaiGetz)
HyundaiGetz.drive(100)
print(HyundaiGetz)
