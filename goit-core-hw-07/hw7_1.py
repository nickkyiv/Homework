from collections import defaultdict, UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        # super().__init__(value)  # TODO: check
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) < 10 and value.isdigit():
            self.__value = value
        else:
            raise ValueError('Invalid phone number, it must be 10 digits long.')


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            return "Please input birthday in DD.MM.YYYY format."


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]

    def add_birthday(self, birthday):
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            print(e)

    def __str__(self):
        if self.birthday:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.date.strftime("%d.%m.%Y")}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find_next_birthday(self, weekday):
        pass
        
    def get_upcoming_birthdays(self):
        prepared_users = []

        for name, record in self.data.items():
            if record.birthday:
                # birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
                prepared_users.append({"name": name, "birthday": record.birthday.date})

    # Функція для визначення, скільки днів додавати для ДН, що припадає на вікенд:
        def find_next_weekday(d): 
            days_to_add = 7 - d.weekday()
            return d + timedelta(days=days_to_add)

        days = 7 # Наступні сім днів для перевірки наявності ДН
        today = datetime.today().date()
        upcoming_birthdays = []

        for user in prepared_users:
            birthday_this_year = user["birthday"].replace(year=today.year)
            if birthday_this_year < today: # якщо ДН минув
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            if 0 <= (birthday_this_year - today).days <= days: # якщо ДН припадає на наст. 7 днів 
                if birthday_this_year.weekday() >= 5: # якщо ДН при цьому припадає на вікенд
                    birthday_this_year = find_next_weekday(birthday_this_year)

                congratulation_date_str = birthday_this_year.strftime("%d.%m.%Y")
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date_str
                })
        
        def generator(data):
            for item in data:
                yield f"{item['name']}: {item['congratulation_date']}"
        
        return_gen = generator(upcoming_birthdays)
        print("The nearest birthdays are:")
        for item in return_gen:
            print(item) #upcoming_birthdays


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "After the command, please input name and phone."
        except IndexError:
            return "After the command, please input name."
        except KeyError:
            return "Please use a correct command. Type 'hello' for list of commands."
    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "This contact does not exist."
    else:
        record.remove_phone(old_phone)
        record.add_phone(new_phone)
        return "Phone number changed."
         

@input_error
def show_phones(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "This contact does not exist."
    else:
        phones = '; '.join(p.value for p in record.phones)
        return f"{name}'s phones are: {phones}"  


@input_error
def show_all(book: AddressBook):
    for name, record in book.data.items():
        print(record)

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    message = "Birthday added."
    if record is None:
        message = "This contact does not exist."
    else:
        record.add_birthday(birthday)
    return message

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "This contact does not exist."
    else:
        return f"{name}'s birthday is {record.birthday.date.strftime("%d.%m.%Y")}"

@input_error
def birthdays(args, book):
    # реалізація
    pass


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot! Type 'hello' to see the list of commands.")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            hello = """Please enter one of the following commands:
- add [name] [phone number]
- change [name] [old number] [new number]
- phone [name]
- all
- add-birthday [name] [birthday] (in DD.MM.YYYY format)
- show-birthday [name]
- birthdays
- hello
- close or exit"""
            print(hello)

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all":
            show_all(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))
            
        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(book.get_upcoming_birthdays())

        else:
            print("Invalid command. Type 'hello' to see the list of commands.")

if __name__ == "__main__":
    main()