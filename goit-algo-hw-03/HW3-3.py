import re

def normalize_phone(x):
    y = re.sub(r"\D", "", x) # removing all non-digits
    if re.search("^380", y): 
        y = re.sub("^380", "+380", y)  # adding + if number starts with "380"
    else: 
        y = re.sub("^0", "+380", y)  # adding +38 if number doesn't start with 38 (starts with 0)
    return y

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)