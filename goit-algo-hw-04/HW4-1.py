def total_salary(path):
    total_s = 0 # Total salary
    times = 0 # Counter of salaries/workers
    with open(path, "r", encoding="utf-8") as file:
        for item in file.readlines():
            _, salary = item.split(",")
            total_s += int(salary) # Total salary calculation
            times += 1
    average_s = total_s / times # Average salary calculation   
    return (total_s, average_s)

print(total_salary('goit-algo-hw-04/hw4-1-salaries.txt'))

