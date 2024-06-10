def main():
    LEN_PASSWARD = 6
    passward = get_passward()
    while len(passward) != LEN_PASSWARD:
        print("Incorrect")
        passward = get_passward()
    display_passward(passward)


def display_passward(passward):
    print(len(passward) * "*")


def get_passward():
    passward = input("Passward: ")
    return passward


main()