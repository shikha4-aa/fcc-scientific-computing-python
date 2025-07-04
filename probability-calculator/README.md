# 🎲 Probability Calculator

This project simulates probability experiments using random draws from a hat. It estimates the chance of drawing a desired combination of colored balls by running a large number of randomized experiments.

---

## 📦 Project Structure

- `Hat` class to manage contents and simulate random draws.
- `experiment()` function to run repeated simulations and calculate probability.
- No external libraries required.

---

## 🚀 How It Works

1. **Initialize a Hat** with any number of colored balls:
   ```python
   hat = Hat(blue=5, red=4, green=2)
