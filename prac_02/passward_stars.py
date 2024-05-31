def main():
    LEN_PASSWARD = 6
    passward = get_passward()
    while len(passward) != LEN_PASSWARD:
        print("Incorrect")
        passward = get_passward()
    method_name(passward)


def method_name(passward):
    print(len(passward) * "*")


def get_passward():
    passward = input("Passward: ")
    return passward


main()