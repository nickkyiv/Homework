import re

def generator_numbers(text):
    for result in re.split(r"\s", text):
        if re.search(r"\d+", result):
            yield float(result)
        else:
            pass

def sum_profit(text, func):
    sum = 0
    for number in func(text):
        sum += number
    return sum

text = """Загальний дохід працівника складається з декількох частин:
1000.01 як основний дохід, доповнений додатковими надходженнями 
27.45 і 324.00 доларів."""

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")