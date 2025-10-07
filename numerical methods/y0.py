def f(x):
    return x ** 3 - x - 3

a = -100.0
b = 100.0
eps = 1e-6  # точність

fa = f(a)
fb = f(b)

if fa * fb > 0:
    print("Функція не змінює знак — кореня на відрізку немає.")
else:
    while abs(b - a) > eps:
        c = (a + b) / 2
        fc = f(c)
        if fa * fc <= 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    print(f"Корінь приблизно x = {(a + b)/2:.6f}")
