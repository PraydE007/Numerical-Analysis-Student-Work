import sys
import numpy as np
from sympy import *  # type: ignore

x = Symbol('x')

def function():
    try:
        expr_input = input("Введіть функцію f(x): ") # x**3 - x - 3
        return sympify(expr_input)
    except SympifyError:
        print("Помилка: некоректний вираз функції.")
        sys.exit(1)
    except Exception as e:
        print(f"Невідома помилка: {e}")
        sys.exit(1)

def secant_method(a, b, f, eps):
    step = 1
    try:
        fa = f.subs(x, a)
        fb = f.subs(x, b)

        if fa == fb:
            print("Помилка: f(a) та f(b) однакові — метод січних не застосовується.")
            return

        while abs(b - a) > eps:
            print(f"Крок {step}: a = {a:.6f}, b = {b:.6f}, f(a) = {fa:.6f}, f(b) = {fb:.6f}")
            # Формула методу січних
            c = b - fb * (b - a) / (fb - fa)
            fc = f.subs(x, c)

            print(f"   Нова точка c = {c:.6f}, f(c) = {fc:.6f}")

            # Оновлюємо точки
            a, b = b, c
            fa, fb = fb, fc

            step += 1
            if step > 1000:
                print("Перевищено кількість ітерацій (1000). Можливо, метод не збігається.")
                break

        print(f"\nПриблизний корінь: x = {b:.6f}")
    except ZeroDivisionError:
        print("Помилка: ділення на нуль (f(b) = f(a)).")
    except Exception as e:
        print(f"Невідома помилка: {e}")

# === Основна частина ===
f = function()

a = -100.0
b = 100.0

eps = float(input("Задайте точність пошуку кореня (epsilon): "))  # Напр. 1e-6
eps = np.clip(eps, sys.float_info.min, 1.0)

secant_method(a, b, f, eps)
