"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_celsius()
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_fahrenheit(fahrenheit)
            celsius = calculate_celsius(celsius, fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_celsius():
    celsius = float(input("Celsius: "))
    return celsius


def calculate_celsius(celsius, fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def get_fahrenheit(fahrenheit):
    fahrenheit = float(input("fahrenheit: "))
    return fahrenheit


def calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()