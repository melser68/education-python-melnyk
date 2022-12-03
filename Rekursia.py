a = int(input('Введіть число до якого вирахувати факторіал: '))

def factorial(a):
    if a <=1:
        return 1
    else:
        return a * factorial(a-1)

print('Факторіал числа ' + str(a) + '! = ' + str(factorial(a)))
