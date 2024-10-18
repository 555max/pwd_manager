master = input("Input master password: ")

def view():
    pass

def add():
    name = input("Account Username: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password)

while True:
    mode = input(
        "Would you like to add a new password or view existing ones? type quit to exit. ").lower()
    if mode == "quit":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
    