counter= int(input("Введите количество билетов: "))

visitors = [int(input("Введите возраст посетителя конференции: ")) for i in range(counter)]
cost = 0
for i in visitors:
    if i >= 18 and i <= 25:
        cost = cost + 990
    elif i > 25:
        cost = cost + 1390
if counter >= 3 and cost > 0:
    cost = cost - (cost /10)
print("Сумма к оплате: ", cost)
