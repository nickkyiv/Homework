#
# Щоб запустити програму, у командному рядку введіть: python hw4-3.py .\Example
#
# Скриншот успішного виконання тут: goit-algo-hw-04\hw43\Screenshot.jpg
# 
import sys
from pathlib import Path
from colorama import Fore, Back

def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        read_folder(path)

def read_folder(path: Path) -> None:
    for item in path.iterdir():
        if item.is_dir():
            print(Back.YELLOW, item, Back.RESET) # Папки виділяємо жовтим фоном
            read_folder(item)
        else:
            print(Fore.BLUE, item, Fore.RESET) # Файли позначаємо синім шрифтом

if __name__ == "__main__":
    main()