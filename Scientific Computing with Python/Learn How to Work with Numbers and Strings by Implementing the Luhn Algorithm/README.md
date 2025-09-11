# Credit Card Validator (Luhn Algorithm)

This Python project validates credit card numbers using the **Luhn algorithm**, a common method used to check the validity of identification numbers such as credit card numbers.

## 🧠 What It Does

- Accepts a credit card number input from the user.
- Cleans the input by removing spaces and dashes.
- Applies the Luhn algorithm to determine if the card number is **valid**.
- Supports user input and includes a set of built-in test cases.

---

## 📜 The Luhn Algorithm

1. Reverse the card number.
2. Add the digits at **odd positions** (from the right).
3. For the **even-positioned digits**, double each digit:
   - If the result is greater than or equal to 10, sum its digits.
4. Add the results from both steps.
5. If the total is divisible by 10, the card number is **valid**.

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.x

### ▶️ Run the script

```bash
python credit_card_validator.py
```

### 🧪 Built-in Test Cases

The script supports test cases like:

4111-1111-4555-1142 ✅ VALID
4222-3333-5444-4211 ❌ INVALID
3782-822463-10005 ✅ VALID
6011-1111-1111-1117 ✅ VALID
5105-1051-0510-5100 ✅ VALID
3782 822463 10005 ✅ VALID
6011 1111 1111 1117 ✅ VALID
