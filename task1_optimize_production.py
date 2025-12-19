import pulp

# Створюємо модель
model = pulp.LpProblem("Drink_Production_Optimization", pulp.LpMaximize)

# Змінні (цілі числа, не менше 0)
L = pulp.LpVariable("Lemonade", lowBound=0, cat=pulp.LpInteger)
F = pulp.LpVariable("FruitJuice", lowBound=0, cat=pulp.LpInteger)

# Цільова функція: максимізувати загальну кількість продуктів
model += L + F, "Total_Products"

# Обмеження на ресурси
model += 2*L + 1*F <= 100, "Water"
model += 1*L <= 50,       "Sugar"
model += 1*L <= 30,       "Lemon_Juice"
model += 2*F <= 40,       "Fruit_Puree"

# Розв'язання
model.solve()

print("Статус розв'язку:", pulp.LpStatus[model.status])
print("Оптимальна кількість лимонаду:", L.varValue)
print("Оптимальна кількість фруктового соку:", F.varValue)
print("Максимальна загальна кількість продуктів:", pulp.value(model.objective))

# Статус розв'язку: Optimal
# Оптимальна кількість лимонаду: 30.0
# Оптимальна кількість фруктового соку: 20.0
# Максимальна загальна кількість продуктів: 50.0