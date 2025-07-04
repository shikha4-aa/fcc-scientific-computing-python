# 🧮 Square Root Finder Using Bisection Method

This Python project uses the **Bisection Method** to approximate the square root of a non-negative number with high precision. It's a clean, numerical method often used when performance and accuracy matter.

---

## ⚙️ How It Works

The bisection method is a **binary search-style algorithm** that narrows down the square root of a number by repeatedly halving the interval between low and high bounds until the desired precision is reached.

### 🧠 Formula Behind It:
We're solving this equation:
x² = N → f(x) = x² - N = 0


We find the root `x` such that `f(x)` is approximately zero.

---

## 🔁 Example Usage

```python
print(sqrt_bisection(25))     # Output: ~5.0
print(sqrt_bisection(0.25))   # Output: ~0.5
print(sqrt_bisection(2))      # Output: ~1.4142


