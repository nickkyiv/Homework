def caching_fibonacci(n: int, cache={}):

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            print(f"Using cache for the value {n}") # Для демонстрації використання кешу
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"writing {n} to cache:", cache) # Для демонстрації запису й наявності кешу
        return cache[n]
        
    return fibonacci(n)

fibonacci = caching_fibonacci
print(f"Число Фібоначчі для 14 дорівнює {fibonacci(14)}") # Розрахунок ведеться лише тут, 
print(f"Число Фібоначчі для 10 дорівнює {fibonacci(10)}") # у наступних принтах дані беруться з кешу
print(f"Число Фібоначчі для 11 дорівнює {fibonacci(11)}")
print(f"Число Фібоначчі для 7 дорівнює {fibonacci(7)}")
print(f"Число Фібоначчі для 14 дорівнює {fibonacci(14)}")