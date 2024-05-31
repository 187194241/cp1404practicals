def main():
    print("(G)et\n(P)rint\n(S)how\n(Q)uit")
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(assess_score(score))
        elif choice == "S":
            print(show_score(score))
        else:
            print("Invalid")
        print("(G)et\n(P)rint\n(S)how\n(Q)uit")
        choice = input("Choice: ").upper()


def get_score():
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid")
        score = float(input("Score: "))
    return score


def assess_score(score):
    while score < 0 or score > 100:
        return "Invalid score"
        score = float(input("Enter score: "))
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


def show_score(score):
    return int(score)*"*"


main()