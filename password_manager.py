master = input("Input master password: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "\n" "Password:", passw)
    

def add():
    name = input("Account Username: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")

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
    