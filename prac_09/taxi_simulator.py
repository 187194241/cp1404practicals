from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return
    try:
        distance = float(input("Drive how far? "))
        fare = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
        return taxi.get_fare()
    except ValueError:
        print("Invalid input")
        return 0


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    while True:
        option = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        if option == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif option == 'c':
            current_taxi = choose_taxi(taxis)
            print(f"Bill to date: ${total_bill:.2f}")
        elif option == 'd':
            fare = drive_taxi(current_taxi)
            total_bill += fare
            print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")


main()
