import random

def get_numbers_ticket(min, max, quantity):
    number_list = []
    try:
        if min >= 1 and max <= 1000:
            while min <= max:
                number_list.append(min)
                min += 1
            win_numbers = random.sample(number_list, quantity)
            # Sorting the list as per this instruction: 
            # Функція повертає список випадково вибраних, __відсортованих__ чисел. 
            win_numbers.sort()
            return win_numbers
        else:
            win_numbers = []
            return win_numbers
    except ValueError:
        print(f"Please use the correct input format: (min, max, quantity)")

x = get_numbers_ticket(1, 50, 6)
print(f"The winning numbers are: {x}")