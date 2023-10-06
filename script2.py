# Функція для знаходження оберненого елементу за модулем p
def inverse_mod(a, p):
    return pow(a, -1, p)

# Функція для подвоєння точки на еліптичній кривій
def elliptic_curve_double(x, y, a, p):
    s = (3 * x * x + a) * inverse_mod(2 * y, p)
    x3 = (s * s - 2 * x) % p
    y3 = (s * (x - x3) - y) % p
    return x3, y3

# Задані параметри кривої
a = -3
p = 31

# Координати точки P
x = 10
y = 17

# Подвоєння точки P
x3, y3 = elliptic_curve_double(x, y, a, p)

# Виведення результату
print(f"Результат подвоєння точки P({x}, {y}): R({x3}, {y3})")