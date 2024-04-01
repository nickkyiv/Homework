from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Invalid phone number. It must be 10 digits long.')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # def input_error(func):
    #     def inner(*args, **kwargs):
    #         try:
    #             return func(*args, **kwargs)
    #         except ValueError:
    #             return "After the command, please input name and phone."
    #         except IndexError:
    #             return "After the command, please input name."
    #         except KeyError:
    #             return "Please use a correct command. Type 'hello' for list of commands."
    #     return inner
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]

    # @input_error
    def add_contact(self, args, address_book):
        name, phone = args
        if name in address_book:
            return f"{name} is already in the Address Book.\nPlease use 'change' command to update the phone."
        else:
            record = Record(name)
            record.add_phone(phone)
            address_book.add_record(record)
            return "Contact added."
    
    # @input_error
    def edit_phone(self, args, address_book): 
        name, old_phone, new_phone = args
        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            record = address_book.get(name)
            record.phones.remove(old_phone)
            record.phones.append(new_phone)   
        return "Contact updated."
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        name = name[0]
        if self.data.get(name):
            return self.data.get(name)
        else:
            return f"{name}'s phone is not in the Address Book."
        
    def delete(self, name):
        if self.data.get(name):
            self.data.pop(name)
            return "Contact deleted."
        else:
            return f"{name}'s phone is not in the Address Book."

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    address_book = AddressBook()
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
            "- edit [name] [old phone number] [new phone number]\n"\
            "- find [name]\n"\
            "- delete [name]\n"\
            "- all\n"\
            "- close or exit"
            print(hello)
        elif command == "add":
            print(Record.add_contact(args, address_book))
        elif command == "edit":
            print(Record.edit_phone(args, address_book))
        elif command == "find":
            print(AddressBook.find(args))
        elif command == "delete":
            print(AddressBook.delete(args))
        elif command == "all":
            print(address_book)
        else:
            print("Invalid command. Type 'hello' to see the list of commands.")

if __name__ == "__main__":
    main()