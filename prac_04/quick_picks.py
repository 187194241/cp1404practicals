import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_EACH_LINE = 6

def print_quick_picks(number):
    for i in range(number):
        numbers = set()
        while len(numbers) < NUMBERS_EACH_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            numbers.add(number)
        numbers = sorted(numbers)
        print(" ".join(f"{number:2}" for number in numbers))

def main():
    number = int(input("How many quick picks? "))
    print_quick_picks(number)

main()