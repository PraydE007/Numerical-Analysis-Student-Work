low = 0
high = 100
guessed = False

while not guessed:
    guess = (low + high) // 2
    print(f"Ваше число - {guess}?")
    feedback = input("Вгадав? Менше? Більше? ")

    if feedback.lower() == "вгадав":
        guessed = True
    elif feedback.lower() == "менше":
        high = guess
    elif feedback.lower() == "більше":
        low = guess
    else:
        print("Будь ласка, введіть 'Вгадав', 'Менше', або 'Більше'.")

if guessed:
    print(f"Я вгадав! Ваше число - {guess}.")