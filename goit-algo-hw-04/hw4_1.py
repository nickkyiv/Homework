# Вміст імпортованого файлу:
# Alex Korp,3000
# Mykyta Borysenko,2000
# Sitarama Raju,1000
# Jack Jones,1500
# Duke Nukem, 1750
# Сума: 9250, середнє: 1850

def total_salary(path):
    total_s = 0 # Total salary
    times = 0 # Counter of salaries/workers
    try:
        with open(path, "r", encoding="utf-8") as file:
            for item in file.readlines():
                _, salary = item.split(",")
                total_s += int(salary) # Total salary calculation
                times += 1
        average_s = total_s / times # Average salary calculation   
        return total_s, average_s
    except (FileNotFoundError, ValueError):
        print("Sorry, missing file or wrong file format.")
try:
    total, average = total_salary('salaries.txt')
    print(f"Загальна сума заробітної плати: {total}, середня заробітна плата: {average}")
except TypeError:
    pass