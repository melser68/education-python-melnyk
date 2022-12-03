arg = input('1_Введіть число або "exit" для виходу: ')

while arg != 'exit':
    try:
        rez = 2 / float(arg)
        print(rez)
        arg = input('2_Введіть число або "exit" для виходу: ')

    except:
        print('Неприпустимий вид даних.')
        arg = input('3_Введіть число або "exit" для виходу: ')
