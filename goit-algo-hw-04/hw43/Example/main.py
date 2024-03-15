from joke import get_random_joke

def main():
    user_name = input("Введіть ваше ім’я: ")
    print(f"Вітаю, {user_name}!")
    
    while True:
        user_response = input(f"{user_name}, хочете анекдот? (так/ні) ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {user_name}!")
            break

if __name__ == "__main__":
    main()