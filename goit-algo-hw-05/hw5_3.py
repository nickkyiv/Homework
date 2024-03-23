import sys
from pathlib import Path
import collections

def main():
    try:
        if len(sys.argv) > 1:
            path = Path(sys.argv[1])
            string_list = load_logs(path)
            level_count = count_logs_by_level(string_list)
            display_log_counts(level_count)
        else:
            quit("Please enter arguments: path (required) and level (optional).")
    except OSError as err:
        print('Помилка доступу до файлу: ', err)
    except ValueError:
        print("Хибний формат файлу.")

    if len(sys.argv) > 2:            
        level_arg = sys.argv[2]
        filtered_list = filter_logs_by_level(string_list, level_arg)
        display_level_info(filtered_list, level_arg)
    
def load_logs(file_path: str) -> list: # для завантаження логів з файлу.
    with open(file_path, "r", encoding="UTF-8") as file:
        string_list = [parse_log_line(string) for string in file.readlines()]
        return string_list

def parse_log_line(line: str) -> dict: # для парсингу рядків логу.
    dictionary = {}
    date, time, level, *msg = line.strip().split(" ")
    dictionary = {"date": date, "time": time, "level": level, "msg": ' '.join(msg)}
    return dictionary

def filter_logs_by_level(logs: list, level: str) -> list: # для фільтрації логів за рівнем.
    filtered_list = [string for string in logs if string["level"].lower() == level.lower()]
    return filtered_list

def count_logs_by_level(logs: list) -> dict: # для підрахунку записів за рівнем логування
    level_count = {}
    for string in logs: 
        if string["level"] in level_count:
            level_count[string["level"]] += 1
        else:
            level_count[string["level"]] = 1
    return level_count

def display_log_counts(counts: dict): # форматує та виводить результати. 
    sorted_dic = dict(sorted(counts.items(), key = lambda item: item[1], reverse = True))
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for item in sorted_dic:
        print(f"{item:<17}| {sorted_dic[item]}")
    print()
    
def display_level_info(logs: list, level: str): # виводить дані для необов’язкового аргумента
    print(f"Записи журнала для рівня {level.upper()}:")
    for dict in logs:
        print(dict["date"], dict["time"], '-', dict["msg"])
    print()

if __name__ == "__main__":
    main()