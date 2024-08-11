from unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("My car", 100, 70)
    distance_driven = my_car.drive(50)

    print(f"Attempted to drive 50 km. Actual distance driven: {distance_driven} km")
    print(my_car)
    distance_driven = my_car.drive(100)

    print(f"Attempted to drive 100 km. Actual distance driven: {distance_driven} km")
    print(my_car)


main()
