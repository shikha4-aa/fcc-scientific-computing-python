# 📐 Polygon Area Calculator

A Python project that uses object-oriented programming to model geometric shapes — **Rectangle** and **Square** — and calculate their properties like area, perimeter, diagonal, and more.

---

## ✅ Features

### 🔷 Rectangle Class

Represents a rectangle defined by its `width` and `height`.

#### Methods:
- `set_width(width)`  
- `set_height(height)`
- `get_area()` → Returns width × height
- `get_perimeter()` → Returns 2 × (width + height)
- `get_diagonal()` → Returns √(width² + height²)
- `get_picture()` → Returns a visual representation using `*`. Max size: 50×50
- `get_amount_inside(other_shape)` → How many times another shape fits inside this one (no rotation)
- `__str__()` → Formatted as: `Rectangle(width=5, height=10)`

---

### 🔳 Square Class

Inherits from `Rectangle`. Initialized with a single `side`. Overrides width/height behavior to ensure both always stay equal.

#### Methods:
- `set_side(side)`
- `set_width(width)` → Sets both width & height
- `set_height(height)` → Sets both width & height
- `__str__()` → Formatted as: `Square(side=9)`


