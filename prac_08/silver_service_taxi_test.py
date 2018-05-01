from prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 300, 2)
print(hummer)
# hummer.drive(30)
# print(hummer)
hummer.start_fare()
hummer.drive(18)
print(hummer.get_fare())