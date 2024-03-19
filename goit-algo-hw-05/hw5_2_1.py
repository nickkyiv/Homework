import re
text = """Загальний дохід працівника складається з декількох частин:
1000.01 як основний дохід, доповнений додатковими надходженнями 
27.45 і 324.00 доларів."""

sum = 0
for result in re.split(r"\s", text):
    if re.search(r"\d+", result):
       sum += float(result)
    else:
        pass
print(sum)