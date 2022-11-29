
def MX(a,b,c):
    if a > b:
        print(a) if a > c else print(c)
    else:
        print(b) if b > c else print(c)
    print('Max')

print('Введите 3 числа. Я посчитаю максимальное')
a, b, c = int(input()), int(input()), int(input())

MX(a,b,c)
