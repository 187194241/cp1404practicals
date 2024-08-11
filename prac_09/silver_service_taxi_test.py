from silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_service_taxi = SilverServiceTaxi("My Car", 200, 2)
    distance_driven = my_silver_service_taxi.drive(18)
    assert distance_driven == 18, f"Expected to drive 18 km, actual drove {distance_driven} km."

    fare = my_silver_service_taxi.get_fare()
    expected_fare = 18 * 2 * 1.23 + 4.50
    assert abs(fare - expected_fare) < 0.01, f"Expected fare: ${expected_fare:.2f}, actual got ${fare:.2f}"

    print(my_silver_service_taxi)
    print(f"Fare for the trip: ${fare:.2f}")


main()
