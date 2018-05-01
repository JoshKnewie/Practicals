from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's Drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    quit_program = ""
    current_taxi = None
    total_bill = 0
    while quit_program != "q":
        menu_selection = input("q)uit, c)hoose taxi, d)rive")
        if menu_selection == "q":
            quit_function(total_bill, taxis)
            quit_program = "q"
        if menu_selection == "c":
            current_taxi = choose_taxi(taxis)
        if menu_selection == "d":
            bill_to_add = drive_taxi(current_taxi)
            total_bill += bill_to_add
        if menu_selection != "q":
            print("Bill to date: $", total_bill)
    print("Goodbye")


def choose_taxi(taxis):
    list_of_taxis(taxis)
    taxi_selection = int(input("Choose taxi"))
    current_taxi = taxis[taxi_selection]
    return current_taxi


def drive_taxi(current_taxi):
    distance_to_drive = int(input("Drive how far?  "))
    current_taxi.drive(distance_to_drive)
    print("Your", current_taxi.name, "cost you", "$", current_taxi.get_fare())
    return current_taxi.get_fare()


def quit_function(total_bill, taxis):
    print("Total trip cost: ${}".format(total_bill))
    print("Taxis are now:")
    list_of_taxis(taxis)


def list_of_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(i, "-", taxi)


main()
