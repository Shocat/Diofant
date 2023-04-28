def solve_dio_eq(a, b, c):
   #Функция, которая решает диофантово уравнение a*x + b*y = c.

    # Используем алгоритм Евклида для нахождения НОД(a, b)
    gcd, x0, y0 = gcd_extended(a, b)

    # Если НОД(a, b) не делит c, то уравнение не имеет целочисленных решений
    if c % gcd != 0:
        return None
    # Находим частное от деления c на НОД(a, b)
    k = c // gcd
    print("k = ", k)

    # Вычисляем x и y
    x = k * x0
    y = k * y0

    # Возвращаем решение
    return x, y

def gcd_extended(a, b):
#Функция, которая находит НОД(a, b) и коэффициенты x и y уравнения a*x + b*y = НОД(a, b).

    if b == 0:
        return a, 1, 0
    else:
        #print("a =", a, "b =", b, "gcd =")
        gcd, x1, y1 = gcd_extended(b, a % b)
        #print("Частное решение x1 и y1 вспомогательного уравнения")

        print("x1 =", x1, "y1 =", y1, "gcd =", gcd)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


# Алгоритм Евклида для нахождения НОД
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a + b

print("Введите коэфициенты a,b,c диофантового уравнения первой степени с двумя неизвестными ax+by=c")
a,b,c = map(int,input().split())
nod = gcd(a,b)
if nod == 1:
    x, y = solve_dio_eq(a, b, c)
    print("Частное решение x0 и y0 исходного уравнения")
    print("x0 =", x, "y0 =", y)
else:
    print("Проверьте правильность введенных коэффициентов a и b", "a и b должны быть взаимно простыми числами", sep=', ')