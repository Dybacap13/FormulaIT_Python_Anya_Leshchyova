money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
reduce = money_capital
while reduce > 0:
    reduce = reduce - spend + salary
    spend *= (increase + 1)
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count - 1)
