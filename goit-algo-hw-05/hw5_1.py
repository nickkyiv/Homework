def caching_fibonacci(n: int, cache={}):

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            print(f"Using cache for the value {n}")
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(cache)
        return cache[n]
        
    return fibonacci(n)

fibonacci = caching_fibonacci
print(f"Число Фібоначчі для 14 дорівнює {fibonacci(14)}")
print(f"Число Фібоначчі для 10 дорівнює {fibonacci(10)}")
print(f"Число Фібоначчі для 11 дорівнює {fibonacci(11)}")
print(f"Число Фібоначчі для 7 дорівнює {fibonacci(7)}")
