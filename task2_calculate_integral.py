import numpy as np
import scipy.integrate as spi
import random

# Функція, яку інтегруємо
def f(x):
    return x**2

a = 0   # нижня межа
b = 2   # верхня межа
N = 100000  # кількість випадкових точок

# 1. Інтеграл методом Монте-Карло
samples = [random.uniform(a, b) for _ in range(N)]
values = [f(x) for x in samples]
mean_f = sum(values) / N
integral_mc = (b - a) * mean_f

print("Оцінка інтеграла методом Монте-Карло:", integral_mc)

# 2. Перевірка через quad
result_quad, error_quad = spi.quad(f, a, b)
print("Інтеграл quad:", result_quad, "похибка quad:", error_quad)

# 3. Аналітичний результат: 
def F(x):
    return x**3 / 3  # первісна для x^2

analytic = F(b) - F(a)

print("Аналітичний:", analytic)

# 4. Порівняння
print("Різниця Monte Carlo - quad:", integral_mc - result_quad)
print("Різниця Monte Carlo - аналітичний:", integral_mc - analytic)

# Оцінка інтеграла методом Монте-Карло: 2.6836394452530574
# Інтеграл quad: 2.6666666666666665 похибка quad: 2.9605947323337504e-14
# Аналітичний: 2.6666666666666665
# Різниця Monte Carlo - quad: 0.016972778586390902
# Різниця Monte Carlo - аналітичний: 0.016972778586390902