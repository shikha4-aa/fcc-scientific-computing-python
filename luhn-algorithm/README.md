# Luhn Algorithm Validator 💳

Implementation of the **Luhn Algorithm**, commonly used to validate identification numbers such as credit card numbers.

### 📌 How It Works:
- Starting from the rightmost digit, double every second digit.
- If the result is greater than 9, subtract 9 from it.
- Sum all the digits.
- If the total modulo 10 is 0, the number is valid.

### 🔍 Example:
Card Number: 4539 1488 0343 6467
Valid: ✅

---

### ✅ Technologies Used:
- Python 3.x
- Plain script (`.py`) – no external libraries

---

This is part of the *Scientific Computing with Python* course by FreeCodeCamp.
