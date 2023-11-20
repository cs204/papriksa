print("Нужная сумма: 50")
a = 50
coin = int(input("Вставьте монету: "))

while a > 0 and a != 0:
    if coin == 50 or coin == 20 or coin == 10 or coin == 5:
        a = a - coin
        if a <= 0: break
        print("Нужная сумма: ",a)
        coin = int(input("Вставьте монету: "))
    else:
        print("Нужная сумма: ",a)
        coin = int(input("Вставьте монету: "))

change_owed = abs (a)
print(f"Ваша сдача: {change_owed}")
