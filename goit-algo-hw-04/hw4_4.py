def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): # Якщо таке ім’я вже є, ф-ція пропонує скористатися командою "change"
    name, phone = args
    if name in contacts:
        return f"{name}'s phone is already in the list.\nPlease use 'change' command to update the phone."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts): # Тут ще більш удосконалено. Якщо користувач хоче змінювати неіснуючий контакт, бот пропонує натомість його створити 
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        user_input = input(f"{name}'s phone is not in the list.\nType 'Y' to add {name}'s phone as a new contact. ")
        if user_input.lower() == "y":
            contacts[name] = phone
            return f"{name}'s phone added to the list."
        else:
            return f""

def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        phone = contacts.get(name)
        return f"{name}'s phone is {phone}"
    else:
        return f"{name}'s phone is not in the list."

def main():
    contacts = {}
    print("Welcome to the assistant bot! Type 'hello' to see the list of commands.")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            hello = "Please enter one of the following commands:\n"\
            "- add [name] [phone number]\n"\
            "- change [name] [phone number]\n"\
            "- phone [name]\n"\
            "- all\n"\
            "- close or exit"
            print(hello)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            # print(args)
            print(show_contact(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command. Type 'hello' to see the list of commands.")

if __name__ == "__main__":
    main()