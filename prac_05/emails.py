"""
Word Occurrences
Estimate: 20 minutes
Actual:   39 minutes
"""
def main():
    users = {}
    while True:
        email = input("Email: ")
        if email == "":
            break
        extract_name = get_extract_name(email)
        confirm = input(f"Is your name {extract_name}? (Y/n) ").lower()
        if confirm == "y":
            users[email] = extract_name
        else:
            correct_name = input("Name: ")
            if correct_name != "":
                users[email] = correct_name
            else:
                print("Name cannot be empty.")
    for email, name in users.items():
        print(f"{name} ({email})")

def get_extract_name(email):
    name = email.split("@")[0]
    name = [part.capitalize() for part in name.split(".")]
    return " ".join(name)

main()