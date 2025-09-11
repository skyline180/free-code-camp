import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def save_result(card_number, status):
    with open("validation_results.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {card_number} -> {status}\n")


def validate_input():
    card_number = entry.get()
    # Remove dashes and spaces
    cleaned = card_number.translate(str.maketrans({'-': '', ' ': ''}))

    if not cleaned.isdigit():
        messagebox.showerror("Invalid Input", "Please enter only digits, dashes, or spaces.")
        return

    result = verify_card_number(cleaned)
    status = "VALID" if result else "INVALID"
    
    messagebox.showinfo("Result", f"Card Number is {status}!")
    save_result(card_number, status)


# GUI Setup
root = tk.Tk()
root.title("Credit Card Validator")

# GUI Layout
tk.Label(root, text="Enter Credit Card Number:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

validate_button = tk.Button(root, text="Validate", command=validate_input)
validate_button.pack(pady=10)

root.mainloop()
