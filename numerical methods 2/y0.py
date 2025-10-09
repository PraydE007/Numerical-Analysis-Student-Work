import sys
import numpy as np
from sympy import * # type: ignore

x = Symbol('x')

def function():
    try:
        # Користувач вводить функцію, наприклад: x**2 + 3*x - 5
        expr_input = input("Введіть функцію f(x): ")
        return sympify(expr_input)
    except SympifyError:
        print("Помилка: некоректний вираз функції.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

def loop(a, b, fa, fb):
    step = 1
    try:
        if fa * fb > 0:
            print("Функція не змінює знак — кореня на відрізку немає.")
        else:
            while abs(b - a) > eps:
                print(f"Крок {step}. Відрізок: {fa:.6f} - {fb:.6f}. Значення: {(a + b)/2:.6f}")
                c = (a + b) / 2
                fc = f.subs(x, c)
                if fa * fc <= 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
                step += 1
            print(f"Корінь приблизно x = {(a + b)/2:.6f}")
    except SympifyError:
        print("Помилка: некоректний вираз функції.")
    except ValueError:
        print("Помилка: некоректне значення x.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

f = function()

a = -100.0
b = 100.0

eps = float(input("Задайте точність пошуку кореня (epsilon): ")) # 1e-6  # точність
eps = np.clip(eps, sys.float_info.min, 1.0)

fa = f.subs(x, a)
fb = f.subs(x, b)

loop(a, b, fa, fb)
