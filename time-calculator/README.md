# 🕒 Time Calculator

A Python function that adds a duration to a starting time and returns the new time in a clean, readable 12-hour clock format. Optionally supports the day of the week and handles transitions like "next day" or "n days later."

---

## Features

- Handles time addition using **12-hour format**
- Calculates overflow across hours, minutes, and days
- Automatically toggles **AM/PM** and wraps around **24-hour periods**
- Supports optional **starting day** input (case-insensitive)
- Appends **(next day)** or **(n days later)** when needed

---

## 🧪 Example Usage

```python
add_time("3:30 PM", "2:12") 
# Returns: "5:42 PM"

add_time("11:59 PM", "24:05")
# Returns: "12:04 AM (2 days later)"

add_time("8:16 PM", "466:02", "tuesday")
# Returns: "6:18 AM, Monday (20 days later)"
