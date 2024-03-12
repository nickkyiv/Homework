import datetime
from datetime import datetime

def get_days_from_today(date):
    now = datetime.today()
    try:
        distant_date = datetime.strptime(date, "%Y-%m-%d")
        # рахуємо чітко у відповідності до вимоги №2:
        # "...Якщо задана дата пізніша за поточну, результат має бути від'ємним."
        difference = now.toordinal() - distant_date.toordinal() 
        return f'The difference between {now.date()} and {date} is {difference} days'
    except (ValueError, UnboundLocalError):
        print("Wrong date format provided. Please use YYYY-MM-DD.")

print(get_days_from_today("2024-05-20"))
print(get_days_from_today("2024-05-21")) # just to check :)