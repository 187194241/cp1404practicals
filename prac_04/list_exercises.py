def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user = input("Enter your username: ")
    if check_user(user, usernames):
        print("Access granted")
        numbers = get_numbers()
        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average number is {sum(numbers) / len(numbers)}")
    else:
        print("Access denied")

def get_numbers():
    global numbers
    numbers = []
    for number in range(5):
        while True:
            try:
                number = float(input("Number: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid number")
    return numbers

def check_user(user, usernames):
    if user in usernames:
        return True
    else:
        return False
main()
