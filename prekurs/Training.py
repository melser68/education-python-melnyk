print('Сервіс ідентифікації для оформлення оренди автомобіля')
age = int(input('Ваш вік: '))
name = input("Ваше ім'я: ")
driver_license = input('Чи маєте Ви водійське посвідчення ? (так, ні) ')
if age >= 18 and driver_license == 'так':
    print(f'{name} Ви можете отримати авто !')
elif driver_license == 'ні':
    print(f'{name} у Вас немає права на керування, у оренді відмовлено')
else:
    print(f'{name} у Вас замалий вік, у оренді відмовлено')