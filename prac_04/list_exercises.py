numbers = []
for number in range(5):
    while True:
        try:
            number = float(input("Number: "))
            break
        except ValueError:
            print("Invalid number")
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers)}")
