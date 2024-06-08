name = input("Name: ")
with open("name.txt", "w") as file:
    file.write(name)
file.close()

with open("name.txt", "r") as file:
    name = file.read()
print(f"Hi {name}!")
file.close()

numbers = [17, 42, 400]
with open("numbers.txt", "w") as file:
    for i in numbers:
        file.write(f"{i}\n")
file.close()

with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print(result)
file.close()

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)
file.close()