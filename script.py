import random

def is_prime(n, k=31):
    """Перевіряє, чи є число n первісним за допомогою тесту Міллера-Рабіна."""
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Представляємо n-1 у вигляді (2^r) * d, де d непарне
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Проводимо k ітерацій тесту Міллера-Рабіна
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

candidates = [16, 17, 18]
chosen_w = None

for w in candidates:
    if is_prime(w):
        chosen_w = w
        break

if chosen_w is not None:
    print(f"Обрано первісний w: {chosen_w}")
else:
    print("Не знайдено первісний w серед кандидатів.")