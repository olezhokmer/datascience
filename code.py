import math
# Функція для знаходження оберненого елементу за модулем p
def inverse_mod(a, p):
    return pow(a, -1, p)

# Функція для подвоєння точки на еліптичній кривій
def elliptic_curve_double(x, y, a, p):
    k = 22
    x2 = (k * k - 2 * x) % p
    y2 = (k * (x - x2) - y) % p
    return x2, y2

# Задані параметри кривої
a = -3
p = 31

# Координати точки P
x1 = 11
y1 = 11

# Подвоєння точки P
x2, y2 = elliptic_curve_double(x1, y1, a, p)

# Виведення результату
print(f"Подвоєння точки P({x1}, {y1}): R({x2}, {y2})")

# Перевірка кандидатів на первісність
candidates = [7, 17, 19]
prime_candidates = []

for candidate in candidates:
    is_prime = True
    for i in range(2, 31):
        print(str(candidate) + '^' + str(i) + ' mod ' + str(31) + ' = ' + str(pow(candidate, i) % 31))
        if pow(candidate, i) % 31 == 1:
            is_prime = False
            break
    if is_prime:
        prime_candidates.append(candidate)

# Виведення первісних кандидатів
print("Первісні кандидати:", prime_candidates)

def find_pow(n1, n2, n3):
    for i in range(1000):
        if pow(n1, i) % n2 == n3:
            return i

print(find_pow(22, 31, 19))