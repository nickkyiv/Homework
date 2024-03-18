def get_cats_info(path):
    list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for item in file.readlines():
                id, name, age = item.strip().split(",")
                dic = {"id": id, "name": name, "age": age}
                list.append(dic)
        return (list)
    except (FileNotFoundError, ValueError):
        print("Sorry, missing file or wrong file format.")
    
cats_info = get_cats_info("cats_info.txt")
print(cats_info)