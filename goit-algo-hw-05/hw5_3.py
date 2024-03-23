import sys
from pathlib import Path

def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    if len(sys.argv) > 2:            
        level_arg = sys.argv[2]

    string_list = load_logs(path)
    level_count = count_logs_by_level(string_list)
        
    filtered_list = filter_logs_by_level(string_list, level_arg)
    
    display_log_counts(level_count)

def parse_log_line(line: str) -> dict: # для парсингу рядків логу.
    dictionary = {}
    date, time, level, *msg = line.strip().split(" ")
    dictionary = {"date": date, "time": time, "level": level, "msg": ' '.join(msg)}
    return dictionary

def load_logs(file_path: str) -> list: # для завантаження логів з файлу.
    with open(file_path, "r", encoding="UTF-8") as file:
        string_list = []
        for string in file.readlines():
            string_list.append(parse_log_line(string))
        return string_list

def filter_logs_by_level(logs: list, level: str) -> list: # для фільтрації логів за рівнем.
    filtered_list = []
    for string in logs:
        if string["level"].lower() == level.lower():
            filtered_list.append(string) 
    return filtered_list

def count_logs_by_level(logs: list) -> dict: # для підрахунку записів за рівнем логування
    level_count = {}
    info = 0
    error = 0 
    debug = 0
    warning = 0
    for string in logs: # INFO, ERROR, DEBUG, WARNING
        if string["level"] == "INFO":
            info += 1
        if string["level"] == "ERROR":
            error += 1
        if string["level"] == "DEBUG":
            debug += 1
        if string["level"] == "WARNING":
            warning += 1
    level_count = {"INFO": info, "ERROR": error, "DEBUG": debug, "WARNING": warning}
    return level_count

def display_log_counts(counts: dict): # яка форматує та виводить результати. 
                                 # Вона приймає результати виконання функції count_logs_by_level
    sorted_dic = dict(sorted(counts.items(), key = lambda item: item[1], reverse = True))
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for item in sorted_dic:
        print(f"{item:<17}| {sorted_dic[item]}")

print(filtered)
    
    







if __name__ == "__main__":
    main()