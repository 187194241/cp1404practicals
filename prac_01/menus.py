name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("hello", name)
    elif choice == "G":
        print("goodbye", name)
    else:
        print("invalid")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()
print("Finished")