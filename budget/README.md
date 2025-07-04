# 💰 Budget App

This project models budgeting categories like Food, Clothing, and Entertainment using OOP in Python. It supports depositing, withdrawing, transferring funds, and visually displays spending via a vertical bar chart.

---

## ✅ Features

### 🧾 `Category` Class
Represents a budget category with the following:

- **`deposit(amount, description='')`**  
  Adds a positive amount to the ledger with an optional description.

- **`withdraw(amount, description='')`**  
  Adds a negative amount if sufficient funds exist. Returns `True` if successful, `False` otherwise.

- **`get_balance()`**  
  Returns current balance based on ledger.

- **`transfer(amount, category)`**  
  Transfers funds to another category if enough balance exists. Logs transfer in both ledgers.

- **`check_funds(amount)`**  
  Returns `True` if enough funds are available, otherwise `False`.

- **`__str__()`**  
  Returns a clean string display of all ledger entries and total.

---

## 📊 `create_spend_chart(categories)`

Creates a **vertical bar chart** showing the **percentage spent** in each category.

- Percentages are based **only on withdrawals**
- Rounded down to nearest **10%**
- Category names are printed **vertically**
- Uses `"o"` characters as bar markers

### 🧠 Chart Example:

Percentage spent by category
100|
90|
80|
70|
60| o
50| o
40| o
30| o
20| o o
10| o o o
0| o o o
----------
F C A
o l u
o o t
d t o
h
i
n
g