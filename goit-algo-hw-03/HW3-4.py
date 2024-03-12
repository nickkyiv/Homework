from datetime import datetime, timedelta

def get_upcoming_birthdays(a):
    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
            prepared_users.append({"name": user["name"], "birthday": birthday})
        except ValueError:
            print(f'Invalid birth date for the user: {user["name"]}')

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

            congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.08"},
    {"name": "Will Smith", "birthday": "1990.03.10"},
    {"name": "Ivanka Trump", "birthday": "1984.03.12"},
    {"name": "Peter Gabriel", "birthday": "1975.03.07"},
    {"name": "George Paine", "birthday": "1994.02.07"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні: ", upcoming_birthdays)